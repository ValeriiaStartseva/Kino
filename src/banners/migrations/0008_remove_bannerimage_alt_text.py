# Generated by Django 5.0.6 on 2024-08-26 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0007_remove_mainpagebanners_gallery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerimage',
            name='alt_text',
        ),
    ]
