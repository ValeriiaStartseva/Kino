# Generated by Django 5.0.6 on 2024-09-10 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_rename_description_ua_movie_description_uk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name_uk',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
