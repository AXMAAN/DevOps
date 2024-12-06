# Generated by Django 3.0.6 on 2020-05-24 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("authentik_flows", "0007_auto_20200703_2059"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsentStage",
            fields=[
                (
                    "stage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="authentik_flows.Stage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Consent Stage",
                "verbose_name_plural": "Consent Stages",
            },
            bases=("authentik_flows.stage",),
        ),
    ]