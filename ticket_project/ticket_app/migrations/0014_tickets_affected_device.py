# Generated by Django 4.0.4 on 2022-06-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0013_alter_devices_device_type_alter_devices_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='affected_device',
            field=models.CharField(default='', max_length=200),
        ),
    ]
