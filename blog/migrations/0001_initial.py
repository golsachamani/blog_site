# Generated by Django 4.2.9 on 2024-01-08 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("text", models.TextField()),
                ("datetime_add", models.DateTimeField(auto_now_add=True)),
                ("datetime_modifie", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("pub", "published"), ("drf", "draft")], max_length=3
                    ),
                ),
                (
                    "aouthor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
