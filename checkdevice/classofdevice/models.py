from django.db import models


class ClassOfDevice(models.Model):
    name = models.CharField('Класс оборудования', max_length=256)

    # add name of class to admin page
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы оборудования'
        db_table = 'device_classes'
