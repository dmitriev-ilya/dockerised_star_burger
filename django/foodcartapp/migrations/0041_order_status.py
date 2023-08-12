# Generated by Django 3.2.15 on 2023-05-12 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0040_auto_20230508_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Н', 'Необработан'), ('С', 'Сборка'), ('Д', 'Доставка'), ('В', 'Выполнен')], default='Н', max_length=1, verbose_name='статус заказа'),
        ),
    ]