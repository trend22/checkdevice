from django.db import models

from intervalcheck.models import IntervalCheck


class TypeOfSi(models.Model):
    name = models.CharField('Тип СИ', max_length=256)
    regNumber = models.CharField('Номер госреестра', max_length=10)
    interval = models.ForeignKey(IntervalCheck, on_delete=models.SET_NULL, null=True)

    # add name of Company to admin page Type of Si
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип СИ'
        verbose_name_plural = 'Типы СИ'
        db_table = 'type_of_sis'
