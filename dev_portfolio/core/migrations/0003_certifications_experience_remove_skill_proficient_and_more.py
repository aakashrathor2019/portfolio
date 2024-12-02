# Generated by Django 4.2.16 on 2024-11-29 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_skill"),
    ]

    operations = [
        migrations.CreateModel(
            name="Certifications",
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
                ("cert_name", models.CharField(max_length=100)),
                ("cert_duration", models.CharField(max_length=50)),
                ("cert_from", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Experience",
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
                ("prj_name", models.CharField(max_length=100)),
                ("prj_link", models.URLField(blank=True, unique=True)),
                ("prj_desc", models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name="skill",
            name="proficient",
        ),
        migrations.AddField(
            model_name="skill",
            name="desc",
            field=models.TextField(null=True),
        ),
    ]
