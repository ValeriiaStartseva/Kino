# Generated by Django 5.0.6 on 2024-07-02 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='type',
        ),
    ]
