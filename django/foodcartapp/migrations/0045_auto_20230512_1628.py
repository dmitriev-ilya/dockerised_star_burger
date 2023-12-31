# Generated by Django 3.2.15 on 2023-05-12 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0044_auto_20230512_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='called_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='перезвонили'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='доставили'),
        ),
        migrations.AlterField(
            model_name='order',
            name='registered_at',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='заказ зарегестрирован'),
        ),
    ]
