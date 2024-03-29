# Generated by Django 4.0.4 on 2022-08-02 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0023_tickets_priority_alter_devices_purchase_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 12, 2, 17, 859673), verbose_name='date purchased'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='state',
            field=models.CharField(choices=[('In warehouse', 'Warehouse'), ('Under repair', 'Repair'), ('Decomissioned', 'Decommissioned'), ('In use', 'In use')], default='In warehouse', max_length=30),
        ),
        migrations.AlterField(
            model_name='devices',
            name='warranty',
            field=models.DateTimeField(default=datetime.datetime(2025, 8, 1, 12, 2, 17, 859684), verbose_name='warranty end'),
        ),
        migrations.AlterField(
            model_name='knowledgearticles',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 12, 2, 17, 860005), verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='opening_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 12, 2, 17, 859861), verbose_name='opening date'),
        ),
    ]
