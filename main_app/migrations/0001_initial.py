# Generated by Django 4.1.6 on 2023-02-07 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('capital_city', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
            ],
        ),
    ]
