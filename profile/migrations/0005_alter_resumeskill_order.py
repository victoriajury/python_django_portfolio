# Generated by Django 5.1.2 on 2024-10-15 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profile", "0004_resumeskill_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resumeskill",
            name="order",
            field=models.IntegerField(auto_created=True),
        ),
    ]