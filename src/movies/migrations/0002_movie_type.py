# Generated by Django 5.0.6 on 2024-07-02 15:55

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('IMAX', 'IMAX'), ('2D', '2D'), ('3D', '3D')], default='3D', max_length=10),
        ),
    ]
