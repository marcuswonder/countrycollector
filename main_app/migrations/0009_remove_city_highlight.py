# Generated by Django 4.1.6 on 2023-02-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_city_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='highlight',
        ),
    ]
