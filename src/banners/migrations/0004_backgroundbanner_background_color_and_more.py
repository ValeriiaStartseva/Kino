# Generated by Django 5.0.6 on 2024-07-30 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0003_mainpagebanners_status_mainpagenewsbanners_status'),
        ('core', '0006_remove_galleryimage_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundbanner',
            name='background_color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='backgroundbanner',
            name='background_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='back_img', to='core.galleryimage'),
        ),
    ]
