# Generated by Django 4.1.6 on 2023-02-08 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_visit_cities_alter_city_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='opulation',
            new_name='population',
        ),
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
