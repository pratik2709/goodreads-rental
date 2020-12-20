from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class TestRentAPIStory1(APITestCase):
    fixtures = ['data.json', 'customer.json', 'version_1.json']

    def setUp(self):
        user = User.objects.get(pk=2)
        Token.objects.get_or_create(user=user)
        self.client.force_login(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user.auth_token.key)

    def test_api_url(self):
        self.assertEqual(reverse('rent_engine:user-books'), '/api/v1/')

    def test_api_successful_response_code(self):
        response = self.client.get(reverse('rent_engine:user-books'))
        self.assertEqual(response.status_code, 200)

    def test_api_data(self):
        response = self.client.get(reverse('rent_engine:user-books'))
        data = response.json()
        expected_data = {'Fiction': 4, 'Regular': 6, 'Novel': 6}
        print(data)
        for key, value in data.items():
            self.assertEqual(expected_data[key], value.get('charges'))


class TestRentAPIStory2(APITestCase):
    fixtures = ['data.json', 'customer.json', 'version_2.json']

    def setUp(self):
        user = User.objects.get(pk=2)
        Token.objects.get_or_create(user=user)
        self.client.force_login(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user.auth_token.key)

    def test_api_url(self):
        self.assertEqual(reverse('rent_engine:user-books'), '/api/v1/')

    def test_api_successful_response_code(self):
        response = self.client.get(reverse('rent_engine:user-books'))
        self.assertEqual(response.status_code, 200)

    def test_api_data(self):
        response = self.client.get(reverse('rent_engine:user-books'))
        data = response.json()
        expected_data = {'Fiction': 30, 'Regular': 15, 'Novel': 15}
        print(data)
        for key, value in data.items():
            self.assertEqual(expected_data[key], value.get('charges'))

class TestRentAPIStory3(APITestCase):
    fixtures = ['data.json', 'customer.json', 'version_3.json']

    def setUp(self):
        user = User.objects.get(pk=2)
        Token.objects.get_or_create(user=user)
        self.client.force_login(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user.auth_token.key)

    def test_api_result(self):
        response = self.client.get(reverse('rent_engine:user-books'))
        data = response.json()
        expected_data = {'Novel': 45.0, 'Regular': 51.5, 'Fiction': 27}
        print(data)
        for key, value in data.items():
            self.assertEqual(expected_data[key], value.get('charges'))
