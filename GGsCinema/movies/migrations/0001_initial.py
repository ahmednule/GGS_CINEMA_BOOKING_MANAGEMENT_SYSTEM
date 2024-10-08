# Generated by Django 5.0.6 on 2024-08-13 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('movie_type', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('director', models.CharField(max_length=100)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='movie_posters/')),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('theater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.theater')),
            ],
        ),
    ]
