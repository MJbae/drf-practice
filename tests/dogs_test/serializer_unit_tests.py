from model_bakery import baker
import json
import pytest

from django.urls import reverse
from django_mock_queries.mocks import MockSet
from rest_framework.relations import RelatedField, SlugRelatedField

from dogs.serializers import TransactionSerializer, CurrencySerializer
from dogs.views import CurrencyViewSet, TransactionViewSet
from dogs.models import Currency, Transaction

pytestmark = [pytest.mark.urls('config.urls'), pytest.mark.unit]


class TestCurrencySerializer:

    def test_serializing_model(self):
        currency = baker.prepare(Currency)
        serializer = CurrencySerializer(currency)

        assert serializer.data

    def test_serialized_data(self):
        currency = baker.prepare(Currency)

        serializer = CurrencySerializer(data=currency.__dict__)

        assert serializer.is_valid()
        assert serializer.errors == {}
