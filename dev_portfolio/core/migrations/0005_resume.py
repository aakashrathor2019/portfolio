# Generated by Django 4.2.16 on 2025-01-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_work_experience"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("resume_data", models.FileField(upload_to="resume_data/")),
            ],
        ),
    ]
