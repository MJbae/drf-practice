# factories.py
import factory
from dogs.models import *


class CurrencyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Currency

    name = factory.faker.Faker('relevant_generator')
    code = factory.faker.Faker('relevant_generator')
    symbol = factory.faker.Faker('relevant_generator')