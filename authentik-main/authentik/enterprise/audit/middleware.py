"""Enterprise audit middleware"""

from copy import deepcopy
from functools import partial
from typing import Any

from django.apps.registry import apps
from django.core.files import File
from django.db import connection
from django.db.models import ManyToManyRel, Model
from django.db.models.expressions import BaseExpression, Combinable
from django.db.models.signals import post_init
from django.http import HttpRequest

from authentik.events.middleware import AuditMiddleware, should_log_model
from authentik.events.utils import cleanse_dict, sanitize_item


class EnterpriseAuditMiddleware(AuditMiddleware):
    """Enterprise audit middleware"""

    @property
    def enabled(self):
        """Check if audit logging is enabled"""
        return apps.get_app_config("authentik_enterprise").enabled()

    def connect(self, request: HttpRequest):
        super().connect(request)
        if not self.enabled:
            return
        if not hasattr(request, "request_id"):
            return
        post_init.connect(
            partial(self.post_init_handler, request=request),
            dispatch_uid=request.request_id,
            weak=False,
        )

    def disconnect(self, request: HttpRequest):
        super().disconnect(request)
        if not self.enabled:
            return
        if not hasattr(request, "request_id"):
            return
        post_init.disconnect(dispatch_uid=request.request_id)

    def serialize_simple(self, model: Model) -> dict:
        """Serialize a model in a very simple way. No ForeignKeys or other relationships are
        resolved"""
        data = {}
        deferred_fields = model.get_deferred_fields()
        for field in model._meta.concrete_fields:
            value = None
            if field.get_attname() in deferred_fields:
                continue

            field_value = getattr(model, field.attname)
            if isinstance(value, File):
                field_value = value.name

            # If current field value is an expression, we are not evaluating it
            if isinstance(field_value, BaseExpression | Combinable):
                continue
            field_value = field.to_python(field_value)
            data[field.name] = deepcopy(field_value)
        return cleanse_dict(data)

    def diff(self, before: dict, after: dict) -> dict:
        """Generate diff between dicts"""
        diff = {}
        for key, value in before.items():
            if after.get(key) != value:
                diff[key] = {"previous_value": value, "new_value": after.get(key)}
        for key, value in after.items():
            if key not in before and key not in diff and before.get(key) != value:
                diff[key] = {"previous_value": before.get(key), "new_value": value}
        return sanitize_item(diff)

    def post_init_handler(self, request: HttpRequest, sender, instance: Model, **_):
        """post_init django model handler"""
        if not should_log_model(instance):
            return
        if hasattr(instance, "_previous_state"):
            return
        before = len(connection.queries)
        instance._previous_state = self.serialize_simple(instance)
        after = len(connection.queries)
        if after > before:
            raise AssertionError("More queries generated by serialize_simple")

    def post_save_handler(
        self,
        request: HttpRequest,
        sender,
        instance: Model,
        created: bool,
        thread_kwargs: dict | None = None,
        **_,
    ):
        if not should_log_model(instance):
            return None
        thread_kwargs = {}
        if hasattr(instance, "_previous_state") or created:
            prev_state = getattr(instance, "_previous_state", {})
            if created:
                prev_state = {}
            # Get current state
            new_state = self.serialize_simple(instance)
            diff = self.diff(prev_state, new_state)
            thread_kwargs["diff"] = diff
        return super().post_save_handler(request, sender, instance, created, thread_kwargs, **_)

    def m2m_changed_handler(  # noqa: PLR0913
        self,
        request: HttpRequest,
        sender,
        instance: Model,
        action: str,
        pk_set: set[Any],
        thread_kwargs: dict | None = None,
        **_,
    ):
        thread_kwargs = {}
        m2m_field = None
        # For the audit log we don't care about `pre_` or `post_` so we trim that part off
        _, _, action_direction = action.partition("_")
        # resolve the "through" model to an actual field
        for field in instance._meta.get_fields():
            if not isinstance(field, ManyToManyRel):
                continue
            if field.through == sender:
                m2m_field = field
        if m2m_field:
            # If we're clearing we just set the "flag" to True
            if action_direction == "clear":
                pk_set = True
            thread_kwargs["diff"] = {m2m_field.related_name: {action_direction: pk_set}}
        return super().m2m_changed_handler(request, sender, instance, action, thread_kwargs)