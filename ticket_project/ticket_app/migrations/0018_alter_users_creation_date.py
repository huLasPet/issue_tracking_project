# Generated by Django 4.0.4 on 2022-06-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0017_alter_users_options_alter_users_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='creation_date',
            field=models.DateTimeField(default='1900-01-01', verbose_name='date created'),
        ),
    ]
