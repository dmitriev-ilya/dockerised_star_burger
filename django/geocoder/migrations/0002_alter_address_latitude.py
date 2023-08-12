# Generated by Django 3.2.15 on 2023-05-14 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geocoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='широта'),
        ),
    ]