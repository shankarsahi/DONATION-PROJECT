# Generated by Django 5.0.3 on 2024-04-02 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GivingWay', '0005_alter_volunteer_adminremark'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='adminremark',
        ),
    ]
