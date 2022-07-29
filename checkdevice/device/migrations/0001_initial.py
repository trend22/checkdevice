# Generated by Django 4.0.6 on 2022-07-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('serialNumber', models.CharField(max_length=50, verbose_name='Серийный номер')),
                ('dateCheck', models.DateField(verbose_name='Дата проверки')),
            ],
            options={
                'verbose_name': 'Техническое средство',
                'verbose_name_plural': 'Технические средства',
                'db_table': 'devices',
            },
        ),
    ]
