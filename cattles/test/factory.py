# factory.py inside users/test
from faker import Faker as FakerClass
from typing import Any, Sequence
from factory.django import DjangoModelFactory

from cattles.models import PublicCattle, SexCategory

SEX_CATEGORIES_VALUES = [x for x in SexCategory.choices]


class PublicCattleFactory(DjangoModelFactory):
    class Meta:
        model = PublicCattle

    birth_date = Faker('birth_date')
    sex = Faker('sex', elements=SEX_CATEGORIES_VALUES)

