# Generated by Django 4.2.7 on 2023-12-03 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: list[tuple] = []

    operations = [
        migrations.CreateModel(
            name="Project",
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
                ("description", models.TextField()),
                ("category", models.CharField(max_length=20)),
                ("date", models.CharField(max_length=20)),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
