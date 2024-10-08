# Generated by Django 5.0.6 on 2024-07-01 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinemas', '0001_initial'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField(db_index=True)),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinemas.hall')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('show_time_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showtimes.showtime')),
            ],
        ),
    ]
