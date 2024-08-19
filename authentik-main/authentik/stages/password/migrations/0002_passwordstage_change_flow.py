# Generated by Django 3.0.7 on 2020-06-29 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_stages_password", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="passwordstage",
            name="change_flow",
            field=models.ForeignKey(
                blank=True,
                help_text=(
                    "Flow used by an authenticated user to change their password. If empty, user"
                    " will be unable to change their password."
                ),
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="authentik_flows.Flow",
            ),
        ),
    ]
