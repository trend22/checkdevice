# Generated by Django 4.0.6 on 2022-07-26 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classofdevice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classofdevice',
            options={'verbose_name': 'Класс', 'verbose_name_plural': 'Классы оборудования'},
        ),
        migrations.AlterModelTable(
            name='classofdevice',
            table='device_classes',
        ),
    ]
