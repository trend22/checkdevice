from django.db import models


class CompanyCheck(models.Model):
    name = models.CharField('Компания-поверитель', max_length=256)

    # add name of Company to admin page CompanyCheck
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поверитель'
        verbose_name_plural = 'Поверители'
        db_table = 'company_checks'
