from django.test import TestCase

from companyuse.models import CompanyUse
from companyuse.serializer import CompanyUseSerializer


class CompanyUseSerializerTestCase(TestCase):
    def test_ok(self):
        '''генерируем данные для сериализатора'''
        company_1 = CompanyUse.objects.create(name='Поверитель 1')
        company_2 = CompanyUse.objects.create(name='Поверитель 2')
        data_serializer = CompanyUseSerializer([company_1, company_2], many=True).data
        data = [
            {
                'id': company_1.id,
                'name': 'Поверитель 1'
            },
            {
                'id': company_2.id,
                'name': 'Поверитель 2'
            },
        ]
        self.assertEqual(data, data_serializer)

