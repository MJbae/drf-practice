from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from cattles.test.factory import PublicCattleFactory
from cattles.models import PublicCattle, SexCategory
from faker import Faker


class UserSignUpTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.public_cattle_object = PublicCattleFactory.build()
        cls.public_cattle_saved = PublicCattleFactory.create()
        cls.faker_obj = Faker()

    def test_if_public_cattle_is_saved_in_db(self):
        public_cattle_dict = {
            'id': self.public_cattle_object.id,
            'birth_date': self.public_cattle_object.birth_date,
            'sex': self.public_cattle_object.sex,
        }
        print(f'public_cattle_dict: {public_cattle_dict}')
        self.assertEqual(self.public_cattle_object.id, self.public_cattle_saved.id)
