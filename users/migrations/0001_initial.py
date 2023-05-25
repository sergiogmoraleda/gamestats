# Generated by Django 4.2.1 on 2023-05-24 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StatsUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('wins', models.IntegerField(blank=True)),
                ('defeat', models.IntegerField(blank=True)),
                ('kda', models.TextField()),
                ('headshotAccuracy', models.FloatField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.TextField(blank=True)),
                ('stats', models.IntegerField(blank=True)),
            ],
        ),
    ]