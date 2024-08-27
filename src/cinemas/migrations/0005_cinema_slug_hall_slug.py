# Generated by Django 5.0.6 on 2024-08-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0004_rename_schema_hall_schema_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='hall',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
