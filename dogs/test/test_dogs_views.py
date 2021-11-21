from django.test import TestCase
from django.urls import reverse
from datetime import timedelta, date

from dogs.models import Dog


class DogListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_dogs = 13

        for dog_id in range(number_of_dogs):
            Dog.objects.create(
                sex='F',
                birth_date=date.today() + timedelta(days=dog_id),
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/v1/dogs/')
        self.assertEqual(response.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     response = self.client.get(reverse('dogs'))
    #     self.assertEqual(response.status_code, 200)


    # def test_pagination_is_ten(self):
    #     response = self.client.get(reverse('authors'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['author_list']) == 10)

    # def test_lists_all_authors(self):
    #     # Get second page and confirm it has (exactly) remaining 3 items
    #     response = self.client.get(reverse('authors') + '?page=2')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('is_paginated' in response.context)
    #     self.assertTrue(response.context['is_paginated'] == True)
    #     self.assertTrue(len(response.context['author_list']) == 3)
