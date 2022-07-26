from django.db import models


class CompanyUse(models.Model):
    name = models.CharField('Компания-эксплуатант', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Эксплуатант'
        verbose_name_plural = 'Эксплуатанты'
        db_table = 'company_uses'
