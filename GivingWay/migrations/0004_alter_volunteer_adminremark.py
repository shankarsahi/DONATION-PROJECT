# Generated by Django 5.0.3 on 2024-04-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GivingWay', '0003_volunteer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='adminremark',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
