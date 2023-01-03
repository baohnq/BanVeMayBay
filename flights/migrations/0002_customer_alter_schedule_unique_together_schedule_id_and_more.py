# Generated by Django 4.1.2 on 2023-01-02 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.CharField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, null=True)),
                ('sdt', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='schedule',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='brand',
            name='brName',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='flId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.flight'),
        ),
        migrations.AddConstraint(
            model_name='schedule',
            constraint=models.UniqueConstraint(fields=('flId', 'date'), name='unique_flId_date_combination'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.customer'),
        ),
    ]