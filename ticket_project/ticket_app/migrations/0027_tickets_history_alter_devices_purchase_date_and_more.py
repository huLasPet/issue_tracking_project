# Generated by Django 4.0.4 on 2022-08-09 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0026_alter_devices_purchase_date_alter_devices_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='history',
            field=models.CharField(default='', max_length=100000),
        ),
        migrations.AlterField(
            model_name='devices',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 10, 19, 20, 367630), verbose_name='date purchased'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='warranty',
            field=models.DateTimeField(default=datetime.datetime(2025, 8, 8, 10, 19, 20, 367644), verbose_name='warranty end'),
        ),
        migrations.AlterField(
            model_name='knowledgearticles',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 10, 19, 20, 367998), verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='opening_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 9, 10, 19, 20, 367835), verbose_name='opening date'),
        ),
    ]
