# Generated by Django 5.1.3 on 2024-11-18 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(default="Anonymous", max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(default="12345", max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "rol",
                    models.CharField(
                        choices=[
                            ("A", "Admin"),
                            ("PM", "Project Manager"),
                            ("D", "Developer"),
                        ],
                        default="D",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                (
                    "developers",
                    models.ManyToManyField(
                        related_name="teams_as_developer", to="project.user"
                    ),
                ),
                (
                    "project_manager",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="teams_as_manager",
                        to="project.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("deadline", models.DateField()),
                ("start_date", models.DateTimeField(auto_now=True)),
                ("observations", models.TextField()),
                ("is_dissabled", models.BooleanField(default=False)),
                ("status", models.CharField(max_length=10)),
                (
                    "priority",
                    models.CharField(
                        choices=[("L", "Lower"), ("M", "Medium"), ("H", "Higher")],
                        default="M",
                        max_length=1,
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="project.team"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="project.user"
                    ),
                ),
            ],
        ),
    ]
