# Generated by Django 4.1.6 on 2023-02-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_remove_country_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='region',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]