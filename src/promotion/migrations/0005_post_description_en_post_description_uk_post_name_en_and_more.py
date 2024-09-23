# Generated by Django 5.0.6 on 2024-09-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0004_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description_uk',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='name_uk',
            field=models.CharField(max_length=40, null=True),
        ),
    ]