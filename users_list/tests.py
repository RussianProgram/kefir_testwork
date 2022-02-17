
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse

"""
Небольно покрытие тестами функций юзера и анонимного юзера
"""
class AnonymousAndUserTest(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user('testuser',
                                                  'test@example@.ru',
                                                  'testpassword')
    def test_anonymous_user_list(self):
        response = self.client.get(reverse('user_list_api'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_login(self):
        data = {
            "username":"testuser",
            "password":"testpassword"
        }
        response = self.client.post(reverse('rest_framework:login'), data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_update(self):
        pk = 1
        data = {
            "username":'testclient'
        }
        response = self.client.post(reverse(viewname="user_detail_api",
                                            kwargs={'pk':pk}),
                                            data=data,
                                            format='json',)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)



