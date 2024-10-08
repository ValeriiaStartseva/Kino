# Generated by Django 5.0.6 on 2024-07-30 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_pages', '0001_initial'),
        ('core', '0006_remove_galleryimage_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=20, unique=True)),
                ('adress_cinema_contacts', models.CharField(max_length=50)),
                ('numbers_contacts', models.CharField(max_length=50)),
                ('email_cinema_contacts', models.CharField(max_length=50)),
                ('coordinates_long', models.CharField(default=0, max_length=12)),
                ('coordinates_lat', models.CharField(default=0, max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('logo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_cinema', to='core.galleryimage')),
            ],
        ),
    ]
