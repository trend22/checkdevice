# Generated by Django 4.0.6 on 2022-07-28 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classofdevice', '0002_alter_classofdevice_options_and_more'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='serialNumber',
            new_name='serial_number',
        ),
        migrations.RemoveField(
            model_name='device',
            name='dateCheck',
        ),
        migrations.AddField(
            model_name='device',
            name='class_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classofdevice.classofdevice'),
        ),
        migrations.AddField(
            model_name='device',
            name='date_check',
            field=models.DateField(null=True, verbose_name='Дата проверки'),
        ),
        migrations.AddField(
            model_name='device',
            name='date_next_check',
            field=models.DateField(null=True, verbose_name='Дата следующей проверки'),
        ),
        migrations.AddField(
            model_name='device',
            name='device_info',
            field=models.TextField(max_length=10000, null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='device',
            name='number_check',
            field=models.CharField(max_length=100, null=True, verbose_name='Реквизит проверки'),
        ),
    ]
