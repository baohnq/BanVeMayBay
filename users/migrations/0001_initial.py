# Generated by Django 4.1.2 on 2022-12-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cusId', models.TextField(max_length=10, primary_key=True, serialize=False)),
                ('cusName', models.TextField(max_length=255)),
                ('cusPhone', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('role', models.IntegerField()),
                ('name', models.TextField()),
            ],
        ),
    ]