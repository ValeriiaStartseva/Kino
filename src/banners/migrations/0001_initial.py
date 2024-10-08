# Generated by Django 5.0.6 on 2024-07-01 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackgroundBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('back', models.CharField(choices=[('option1', 'css'), ('option2', 'photo')], max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='BannersGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_group_types', models.CharField(choices=[('main_top', 'main_top'), ('news_promotion', 'news_promotion')], max_length=14)),
                ('rotation_speed', models.IntegerField()),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.gallery')),
            ],
        ),
    ]
