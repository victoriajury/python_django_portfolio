# Generated by Django 5.1.2 on 2024-10-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0006_remove_resumeskill_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="resumeskill",
            name="position",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]