from django.test import TestCase

from classofdevice.models import ClassOfDevice
from classofdevice.serializer import ClassOfDeviceSerializer


class CompanyCheckSerializerTestCase(TestCase):
    '''проверка сериалайзера модели CompanyCheck'''
    def test_ok(self):
        '''генерируем данные для сериализатора'''
        class_1 = ClassOfDevice.objects.create(name='СИ')
        class_2 = ClassOfDevice.objects.create(name='ИО')
        data = ClassOfDeviceSerializer([class_1, class_2], many=True).data
        '''генерируем ожидаемую информацию'''
        expected_data = [
            {
                'id': class_1.id,
                'name': 'СИ',
            },
            {
                'id': class_2.id,
                'name': 'ИО',
            },
        ]
        self.assertEqual(data, expected_data)
