import json

from django.test import TestCase


from intervalcheck.models import IntervalCheck
from intervalcheck.serializer import IntervalCheckSerializer


class IntervalCheckSerializerTestCase(TestCase):
    def test_ok(self):
        '''генерируем данные для сериализатора'''
        interval_1 = IntervalCheck.objects.create(interval=1)
        interval_2 = IntervalCheck.objects.create(interval=2)
        data_serializer = IntervalCheckSerializer([interval_1, interval_2], many=True).data
        data = [
            {
                'id': interval_1.id,
                'interval': '1.0'
            },
            {
                'id': interval_2.id,
                'interval': '2.0'
            },
        ]
        self.assertEqual(data, data_serializer)
