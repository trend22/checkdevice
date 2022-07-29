from django.contrib.auth.models import User
from django.db import models

from classofdevice.models import ClassOfDevice
from companycheck.models import CompanyCheck
from companyuse.models import CompanyUse
from typeofsi.models import TypeOfSi


class Device(models.Model):
    name = models.CharField('Наименование', max_length=200)
    serial_number = models.CharField('Серийный номер',  max_length=50)
    date_check = models.DateField('Дата проверки', null=True)
    date_next_check = models.DateField('Дата следующей проверки', null=True)
    number_check = models.CharField('Реквизит проверки', max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default='admin', verbose_name='права')
    class_device = models.ForeignKey(ClassOfDevice, on_delete=models.SET_NULL, null=True,
                                     verbose_name='класс технического средства')
    type = models.ForeignKey(TypeOfSi, on_delete=models.SET_NULL, null=True, verbose_name='Тип СИ')
    who_check = models.ForeignKey(CompanyCheck, on_delete=models.SET_NULL, null=True,
                                  verbose_name='поверитель')
    who_use = models.ForeignKey(CompanyUse, on_delete=models.SET_NULL, null=True,
                                verbose_name='эксплуатант')
    device_info = models.TextField('Дополнительная информация', max_length=10000, null=True)

    # def is_si(self):
    #     if self.type:


    class Meta:
        verbose_name = 'Техническое средство'
        verbose_name_plural = 'Технические средства'
        db_table = 'devices'
