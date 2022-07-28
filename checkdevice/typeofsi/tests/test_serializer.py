import json

from django.test import TestCase

from intervalcheck.models import IntervalCheck
from typeofsi.models import TypeOfSi
from typeofsi.serializer import TypeOfSiSerializer


class TypeOfSiSerializerTestCase(TestCase):
    def test_ok(self):
        '''генерируем интервалы IntervalCheck'''
        interval_1 = IntervalCheck.objects.create(interval=1)
        interval_2 = IntervalCheck.objects.create(interval=2)
        '''генерируем данные для сериализатора'''
        type_1 = TypeOfSi.objects.create(name='мультиметр', regNumber='10000-01', interval=interval_1)
        type_2 = TypeOfSi.objects.create(name='клещи', regNumber='20000-02', interval=interval_2)
        '''Тип СИ 3 создаётся с нулевым интервалом'''
        type_3 = TypeOfSi.objects.create(name='источник питания', regNumber='30000-30')
        data_serializer = TypeOfSiSerializer([type_1, type_2, type_3], many=True).data
        data = [
            {
                'id': type_1.id,
                'name': 'мультиметр',
                'regNumber': '10000-01',
                'interval': 1
            },
            {
                'id': type_2.id,
                'name': 'клещи',
                'regNumber': '20000-02',
                'interval': 2
            },
            {
                'id': type_3.id,
                'name': 'источник питания',
                'regNumber': '30000-30',
                'interval': None
            },
        ]
        self.assertEqual(data, data_serializer)
