# Generated by Django 5.0.6 on 2024-09-10 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_rename_description_uk_movie_description_ua_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='description_ua',
            new_name='description_uk',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='name_ua',
            new_name='name_uk',
        ),
    ]
