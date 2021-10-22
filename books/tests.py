from django.urls import reverse
from django_seed import Seed

from .models import Author, Book
from rest_framework.test import APITestCase

seeder = Seed.seeder()


class BooksTestCase(APITestCase):
    def test_list_books(self):
        # Add dummy data to the Author and Book Table
        seeder.add_entity(Author, 5)
        seeder.add_entity(Book, 10)
        seeder.execute()
        # we expect the result in 1 query
        with self.assertNumQueries(1):
            response = self.client.get(reverse("book_list"), format="json")
