from django.urls import include, path, reverse
from dogs.models import Dog
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from datetime import date, timedelta


class DogTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.URL_DOGS = "/api/v1/dogs/"
        cls.TARGET_DOG_ID = "1"
        number_of_dogs = 3

        for dog_id in range(number_of_dogs):
            Dog.objects.create(
                sex='F',
                birth_date=date.today() + timedelta(days=dog_id),
            )

    def test_create_and_retrieve_dog(self):
        # test create-feature
        birth_date = date.today()
        data = {"birth_date": birth_date, "sex": "F"}
        response = self.client.post(self.URL_DOGS, data, format='json')
        created_dog_id = response.data['id']

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.get(id=created_dog_id).birth_date, birth_date)
        self.assertEqual(Dog.objects.get(id=created_dog_id).sex, 'F')

        # test retrieve-feature
        url = self.URL_DOGS + f'{created_dog_id}' + "/"
        response = self.client.get(url, format='json')
        retrieved_dog_birth_date = response.data['birth_date']
        retrieved_dog_sex = response.data['sex']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(retrieved_dog_birth_date, birth_date.strftime('%Y-%m-%d'))
        self.assertEqual(retrieved_dog_sex, 'F')

    def test_retrieve_dogs(self):
        number_of_objects_in_model = Dog.objects.count()
        response = self.client.get(self.URL_DOGS, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), number_of_objects_in_model)

    def test_update_dog(self):
        # test create-feature
        birth_date = date.today()
        sex = "M"
        data = {"birth_date": birth_date, "sex": sex}
        target_dog_id = self.TARGET_DOG_ID

        # test retrieve-feature
        url = self.URL_DOGS + f'{target_dog_id}' + "/"
        response = self.client.patch(url, data, format='json')
        returned_birth_date = response.data['birth_date']
        returned_dog_sex = response.data['sex']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(returned_birth_date, birth_date.strftime('%Y-%m-%d'))
        self.assertEqual(returned_dog_sex, sex)
