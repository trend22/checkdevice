import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from intervalcheck.models import IntervalCheck
from typeofsi.models import TypeOfSi
from typeofsi.serializer import TypeOfSiSerializer


class TypeOfSiApiTestCase(APITestCase):
    def setUp(self):
        '''Для каждого ниже теста setUp создаёт свои копии и ID'''
        '''При этом тесты проходят по своему внутреннего порядковому номеру'''
        '''создаем user's для тестов'''
        self.user = User.objects.create(username='test_user', password='12345')
        self.user_staff = User.objects.create(username='test_admin', password='admin', is_staff=True)
        '''генерируем интервалы IntervalCheck'''
        self.interval_1 = IntervalCheck.objects.create(interval=1)
        self.interval_2 = IntervalCheck.objects.create(interval=2)
        '''генерируем данные для сериализатора'''
        self.type_1 = TypeOfSi.objects.create(name='мультиметр', regNumber='10000-01', interval=self.interval_1)
        self.type_2 = TypeOfSi.objects.create(name='клещи', regNumber='20000-02', interval=self.interval_2)
        '''Тип СИ 3 создаётся с нулевым интервалом'''
        self.type_3 = TypeOfSi.objects.create(name='источник питания', regNumber='30000-30')

    def test_get_all(self):
        '''логиним пользователя'''
        self.client.force_login(self.user)
        url = reverse('typeofsi-list')
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.get(url)
        '''проверка на создание компаний'''
        '''чтобы не копировать сюда ответ от CompanyCheckSerializer'''
        '''импортируем serializer и будет его здесь использовать'''
        serializer_data = TypeOfSiSerializer([self.type_1, self.type_2, self.type_3], many=True).data
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_one(self):
        '''логиним пользователя'''
        self.client.force_login(self.user)
        url = reverse('typeofsi-detail', args=(self.type_1.id,))
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.get(url)
        '''проверка на создание компаний'''
        '''чтобы не копировать сюда ответ от CompanyCheckSerializer'''
        '''импортируем serializer и будет его здесь использовать'''
        serializer_data = TypeOfSiSerializer(self.type_1).data
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(3, TypeOfSi.objects.all().count())
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        url = reverse('typeofsi-list')
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        interval_4 = IntervalCheck.objects.create(interval=4)
        type_4 = {
            'id': 4,
            'name': 'Измеритель мощности',
            'regNumber': '40000-40',
            'interval': interval_4.id
        }
        data_json = json.dumps(type_4)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.post(url, data=data_json, content_type='application/json')
        '''импортируем status из rest framework'''
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, TypeOfSi.objects.all().count())
        self.assertEqual(type_4, response.data)

    def test_create_not_staff(self):
        self.assertEqual(3, TypeOfSi.objects.all().count())
        '''логиним обычного пользователя'''
        self.client.force_login(self.user)
        url = reverse('typeofsi-list')
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        interval_4 = IntervalCheck.objects.create(interval=4)
        type_4 = {
            'id': 4,
            'name': 'Измеритель мощности',
            'regNumber': '40000-40',
            'interval': interval_4.id
        }
        data_json = json.dumps(type_4)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.post(url, data=data_json, content_type='application/json')
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(3, TypeOfSi.objects.all().count())

    def test_put(self):
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        '''передаём в url id компании'''
        url = reverse('typeofsi-detail', args=(self.type_3.id,))
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        '''В data.interval пишем self.interval_2.id - его создаёт setUp'''
        data = {
            'id': self.type_3.id,
            'name': 'источник питания',
            'regNumber': '30000-30',
            'interval': self.interval_2.id
        }

        data_json = json.dumps(data)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.put(url, data=data_json, content_type='application/json')

        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        '''обновляем изменённый interval_1 в классе test'''
        self.type_3.refresh_from_db()
        self.assertEqual(self.interval_2.id, self.type_3.interval.id)

    def test_put_not_staff(self):
        '''логиним обычного пользователя'''
        self.client.force_login(self.user)
        '''передаём в url id компании'''
        url = reverse('typeofsi-detail', args=(self.type_3.id,))
        '''Создаём данные для POST запроса и делаем даныые json формата'''
        data = {
            'id': self.type_3.id,
            'name': 'источник питания',
            'regNumber': '30000-30',
            'interval': self.interval_2.id
        }
        data_json = json.dumps(data)
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.put(url, data=data_json, content_type='application/json')
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        '''обновляем изменённый company_1 в классе test'''
        self.type_3.refresh_from_db()
        self.assertEqual(None, self.type_3.interval)

    def test_delete(self):
        self.assertEqual(3, TypeOfSi.objects.all().count())
        '''логиним пользователя'''
        self.client.force_login(self.user_staff)
        url = reverse('typeofsi-detail', args=(self.type_2.id,))
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.delete(url)
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(2, TypeOfSi.objects.all().count())

    def test_delete_not_staff(self):
        self.assertEqual(3, TypeOfSi.objects.all().count())
        '''логиним обычного пользователя'''
        self.client.force_login(self.user)
        url = reverse('typeofsi-detail', args=(self.type_2.id,))
        '''self.client - в роли клиента выступает браузер, который даёт данные c url'''
        response = self.client.delete(url)
        '''ипортируем status из rest framework'''
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(3, TypeOfSi.objects.all().count())
