from django.urls import include, path, reverse
from dogs.models import Dog
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from datetime import date, timedelta


class DogTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/v1/', include('dogs.urls')),
    ]

    def test_create_dog(self):
        length_before = Dog.objects.count()
        url = reverse('dogs-list')
        birth_date = date.today()
        data = {"birth_date": birth_date, "sex": "F"}
        response = self.client.post(url, data, format='json')
        print(f'response: {response}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), length_before + 1)
        self.assertEqual(Dog.objects.get().birth_date, birth_date)
        self.assertEqual(Dog.objects.get().sex, 'F')

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('dogs-list'))
        self.assertEqual(response.status_code, 200)
