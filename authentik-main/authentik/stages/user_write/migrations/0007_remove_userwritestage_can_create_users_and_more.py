# Generated by Django 4.1.5 on 2023-01-05 12:34

from django.apps.registry import Apps
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def migrate_to_user_creation_mode(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    UserWriteStage = apps.get_model("authentik_stages_user_write", "userwritestage")
    from authentik.stages.user_write.models import UserCreationMode

    for stage in UserWriteStage.objects.using(schema_editor.connection.alias).all():
        if stage.can_create_users:
            stage.user_creation_mode = UserCreationMode.CREATE_WHEN_REQUIRED
        else:
            stage.user_creation_mode = UserCreationMode.NEVER_CREATE
        stage.save()


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_user_write", "0006_userwritestage_can_create_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="userwritestage",
            name="user_creation_mode",
            field=models.TextField(
                choices=[
                    ("never_create", "Never Create"),
                    ("create_when_required", "Create When Required"),
                    ("always_create", "Always Create"),
                ],
                default="create_when_required",
            ),
        ),
        migrations.RunPython(migrate_to_user_creation_mode),
        migrations.RemoveField(
            model_name="userwritestage",
            name="can_create_users",
        ),
    ]