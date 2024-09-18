# Generated by Django 5.0.6 on 2024-09-11 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pages', '0007_rename_description_ua_page_description_uk_and_more'),
        ('core', '0006_remove_galleryimage_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.gallery'),
        ),
    ]
