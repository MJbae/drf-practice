from django.test import TestCase
from django.urls import reverse
from datetime import timedelta, date

from dogs.models import Dog


class DogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.URL_DOGS = "/api/v1/dogs/"
        # Create 13 dogs for pagination tests
        number_of_dogs = 13

        for dog_id in range(number_of_dogs):
            Dog.objects.create(
                sex='F',
                birth_date=date.today() + timedelta(days=dog_id),
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(self.URL_DOGS)
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(self.URL_DOGS)
        self.assertEqual(response.status_code, 200)

