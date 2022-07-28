from django.test import TestCase

from companycheck.models import CompanyCheck
from companycheck.serializer import CompanyCheckSerializer


class CompanyCheckSerializerTestCase(TestCase):
    '''проверка сериалайзера модели CompanyCheck'''
    def test_ok(self):
        '''генерируем данные для сериализатора'''
        company_1 = CompanyCheck.objects.create(name='Поверитель 1')
        company_2 = CompanyCheck.objects.create(name='Поверитель 2')
        data = CompanyCheckSerializer([company_1, company_2], many=True).data
        '''генерируем ожидаемую информацию'''
        expected_data = [
            {
                'id': company_1.id,
                'name': 'Поверитель 1',
            },
            {
                'id': company_2.id,
                'name': 'Поверитель 2',
            },
        ]
        self.assertEqual(data, expected_data)
