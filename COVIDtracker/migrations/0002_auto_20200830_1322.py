# Generated by Django 3.0.8 on 2020-08-30 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('COVIDtracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='failed_api_calls',
        ),
        migrations.RemoveField(
            model_name='user',
            name='successfull_api_calls',
        ),
    ]
