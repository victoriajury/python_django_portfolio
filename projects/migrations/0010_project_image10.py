# Generated by Django 5.1.2 on 2024-10-14 19:48

import projects.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0009_project_image7_project_image8_project_image9"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image10",
            field=models.FileField(
                blank=True,
                upload_to=projects.models.project_image_directory,
                verbose_name="Image 10",
            ),
        ),
    ]