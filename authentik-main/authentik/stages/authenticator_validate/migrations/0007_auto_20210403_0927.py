# Generated by Django 3.1.7 on 2021-04-03 09:27

import django.contrib.postgres.fields
from django.db import migrations, models

import authentik.stages.authenticator_validate.models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_authenticator_validate", "0006_auto_20210301_1757"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authenticatorvalidatestage",
            name="device_classes",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(
                    choices=[
                        ("static", "Static"),
                        ("totp", "TOTP"),
                        ("webauthn", "WebAuthn"),
                    ]
                ),
                default=authentik.stages.authenticator_validate.models.default_device_classes,
                help_text="Device classes which can be used to authenticate",
                size=None,
            ),
        ),
    ]