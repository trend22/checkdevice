import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from companyuse.models import CompanyUse
from companyuse.serializer import CompanyUseSerializer


class CompanyUseApiTestCase(APITestCase):
    def setUp(self):
        '''создаем данные для тестов'''
        self.user = User.objects.create(username='test_user', password='12345')
        self.user_staff = User.objects.create(username='test_admin', password='admin', is_staff=True)
        self.company_1 = CompanyUse.objects.create(name='Эксплуатант 1')
        self.company_2 = CompanyUse.objects.create(name='Эксплуатант 2')

    def test_get_all(self):
        '''логиним пользователя'''
        self.client.force_login(self.user)
        url = reverse('companyuse-list')
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.get(url)
        '''проверка на создание компаний'''
        '''чтобы не копировать сюда ответ от CompanyCheckSerializer'''
        '''импортируем serializer и будет его здесь использовать'''
        serializer_data = CompanyUseSerializer([self.company_1, self.company_2], many=True).data
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_one(self):
        '''логиним пользователя'''
        self.client.force_login(self.user)
        url = reverse('companyuse-detail', args=(self.company_1.id,))
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.get(url)
        '''проверка на создание компаний'''
        '''чтобы не копировать сюда ответ от CompanyCheckSerializer'''
        '''импортируем serializer и будет его здесь использовать'''
        serializer_data = CompanyUseSerializer(self.company_1).data
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, CompanyUse.objects.all().count())
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        url = reverse('companyuse-list')
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        company_3 = {
            'name': 'Эксплуатант 3'
        }
        data_json = json.dumps(company_3)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.post(url, data=data_json, content_type='application/json')
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, CompanyUse.objects.all().count())

    def test_put(self):
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        '''передаём в url id компании'''
        url = reverse('companyuse-detail', args=(self.company_1.id,))
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        data = {
            'name': 'Эксплуатант 1 (лучший эксплуатант)'
        }
        data_json = json.dumps(data)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.put(url, data=data_json, content_type='application/json')
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        '''обновляем изменённый company_1 в классе test'''
        self.company_1.refresh_from_db()
        self.assertEqual('Эксплуатант 1 (лучший эксплуатант)', self.company_1.name)

    def test_delete(self):
        self.assertEqual(2, CompanyUse.objects.all().count())
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        url = reverse('companyuse-detail', args=(self.company_2.id,))
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.delete(url)
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(1, CompanyUse.objects.all().count())
