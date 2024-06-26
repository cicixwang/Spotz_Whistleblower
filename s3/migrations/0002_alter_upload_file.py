# Generated by Django 5.0.3 on 2024-03-15 17:01

import s3.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("s3", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="upload",
            name="file",
            field=models.FileField(
                upload_to="", validators=[s3.models.Upload.validate_mime_type]
            ),
        ),
    ]
