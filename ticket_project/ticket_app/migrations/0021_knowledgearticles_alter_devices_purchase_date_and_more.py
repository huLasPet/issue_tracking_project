# Generated by Django 4.0.4 on 2022-07-12 08:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0020_tickets_opening_date_alter_devices_purchase_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnowledgeArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100000)),
                ('state', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=20)),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2022, 7, 12, 10, 47, 6, 258565), verbose_name='Creation date')),
                ('created_by', models.CharField(max_length=200)),
                ('modified_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='devices',
            name='purchase_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 12, 10, 47, 6, 258242), verbose_name='date purchased'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='warranty',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 11, 10, 47, 6, 258254), verbose_name='warranty end'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='opening_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 12, 10, 47, 6, 258431), verbose_name='opening date'),
        ),
    ]
