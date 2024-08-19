# Generated by Django 4.0 on 2021-12-22 09:42

import uuid

import django.db.models.deletion
from django.db import migrations, models

import authentik.lib.utils.time


class Migration(migrations.Migration):
    replaces = [
        ("authentik_brands", "0001_initial"),
        ("authentik_brands", "0002_default"),
        ("authentik_brands", "0003_tenant_branding_favicon"),
        ("authentik_brands", "0004_tenant_event_retention"),
        ("authentik_brands", "0005_tenant_web_certificate"),
    ]

    initial = True

    dependencies = [
        ("authentik_crypto", "0003_certificatekeypair_managed"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "tenant_uuid",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "domain",
                    models.TextField(
                        help_text=(
                            "Domain that activates this brand. Can be a superset, i.e. `a.b` for"
                            " `aa.b` and `ba.b`"
                        )
                    ),
                ),
                ("default", models.BooleanField(default=False)),
                ("branding_title", models.TextField(default="authentik")),
                (
                    "branding_logo",
                    models.TextField(default="/static/dist/assets/icons/icon_left_brand.svg"),
                ),
                (
                    "flow_authentication",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand_authentication",
                        to="authentik_flows.flow",
                    ),
                ),
                (
                    "flow_invalidation",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand_invalidation",
                        to="authentik_flows.flow",
                    ),
                ),
                (
                    "flow_recovery",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand_recovery",
                        to="authentik_flows.flow",
                    ),
                ),
                (
                    "flow_unenrollment",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand_unenrollment",
                        to="authentik_flows.flow",
                    ),
                ),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brands",
            },
        ),
        migrations.AddField(
            model_name="brand",
            name="branding_favicon",
            field=models.TextField(default="/static/dist/assets/icons/icon.png"),
        ),
        migrations.AddField(
            model_name="brand",
            name="event_retention",
            field=models.TextField(
                default="days=365",
                help_text=(
                    "Events will be deleted after this duration.(Format:"
                    " weeks=3;days=2;hours=3,seconds=2)."
                ),
                validators=[authentik.lib.utils.time.timedelta_string_validator],
            ),
        ),
        migrations.AddField(
            model_name="brand",
            name="web_certificate",
            field=models.ForeignKey(
                default=None,
                help_text="Web Certificate used by the authentik Core webserver.",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="authentik_crypto.certificatekeypair",
            ),
        ),
    ]
