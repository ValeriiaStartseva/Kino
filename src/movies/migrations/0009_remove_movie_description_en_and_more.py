# Generated by Django 5.0.6 on 2024-09-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_movie_name_alter_movie_name_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='description_uk',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='name_uk',
        ),
    ]
