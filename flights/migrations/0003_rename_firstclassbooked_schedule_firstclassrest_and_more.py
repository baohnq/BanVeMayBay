# Generated by Django 4.1.4 on 2023-01-03 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_customer_alter_schedule_unique_together_schedule_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='firstClassBooked',
            new_name='firstClassRest',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='secondClassBooked',
            new_name='secondClassRest',
        ),
    ]