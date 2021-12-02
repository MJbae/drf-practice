from django.urls import include, path, reverse
from dogs.models import Dog
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from datetime import date, timedelta


class DogTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.URL_DOGS = "/api/v1/dogs/"

    def test_create_and_retrieve_dog(self):
        number_of_objects_before_test = Dog.objects.count()
        birth_date = date.today()
        data = {"birth_date": birth_date, "sex": "F"}
        response = self.client.post(self.URL_DOGS, data, format='json')
        print(f'response: {response}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), number_of_objects_before_test + 1)
        self.assertEqual(Dog.objects.get().birth_date, birth_date)
        self.assertEqual(Dog.objects.get().sex, 'F')

    def test_retrieve_dogs(self):
        number_of_objects_in_model = Dog.objects.count()
        response = self.client.get(self.URL_DOGS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), number_of_objects_in_model)

    def test_retrieve_dog(self):
        url = self.URL_DOGS + "1/"
        response = self.client.get(self.URL_DOGS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
