# factories.py
import factory

from factory.faker import faker
from dogs.models import *


class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    name = factory.Sequence(lambda n: "Bae%s" % n)
    code = factory.Sequence(lambda n: "%s" % n)
    symbol = factory.Sequence(lambda n: "%s" % n)
