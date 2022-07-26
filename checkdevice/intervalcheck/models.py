from django.db import models


class IntervalCheck(models.Model):
    interval = models.DecimalField('Интервал проверки, год', max_digits=3, decimal_places=1)

    # add name of Company to admin page CompanyCheck
    def __str__(self):
        return '{}'.format(self.interval)

    class Meta:
        verbose_name = 'Интервал'
        verbose_name_plural = 'Интервалы'
        db_table = 'interval_checks'
