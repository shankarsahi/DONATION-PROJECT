# Generated by Django 5.0.3 on 2024-04-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GivingWay', '0008_volunteer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='user',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='user',
        ),
    ]
