# Generated by Django 4.0.4 on 2022-06-01 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0008_alter_tickets_ticket_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='ticket_number',
        ),
    ]
