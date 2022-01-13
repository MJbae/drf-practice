from model_bakery import baker
import json
import pytest

from django.urls import reverse
from django_mock_queries.mocks import MockSet
from rest_framework.relations import RelatedField, SlugRelatedField

from dogs.serializers import (
    UnfilledTransactionSerializer,
    FilledTransactionSerializer,
    CurrencySerializer,
)
from dogs.views import CurrencyViewSet, TransactionViewSet
from dogs.models import Currency, Transaction

pytestmark = [pytest.mark.urls("config.urls"), pytest.mark.unit]


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


class TestUnfilledTransactionSerializer:
    @pytest.mark.django_db
    def test_serializing_model(self, utbbnp):
        t = baker.make(
            "dogs.Transaction",
            currency=baker.make("dogs.Currency"),
            _fill_optional=["name", "email", "currency", "message"],
        )
        expected_serialized_data = {
            "name": t.name,
            "currency": t.currency.id,
            "email": t.email,
            "message": t.message,
        }

        serializer = UnfilledTransactionSerializer(t)

        assert serializer.data["name"] == expected_serialized_data["name"]
        assert serializer.data["currency"] == expected_serialized_data["currency"]
        assert serializer.data["email"] == expected_serialized_data["email"]
        assert serializer.data["message"] == expected_serialized_data["message"]

    @pytest.mark.django_db
    def test_serialized_data(self, mocker):
        t = baker.prepare(
            "dogs.Transaction",
            currency=baker.make("dogs.Currency"),
            _fill_optional=["name", "email", "currency", "message"],
        )
        valid_serialized_data = {
            "name": t.name,
            "currency": t.currency.id,
            "email": t.email,
            "message": t.message,
        }

        serializer = UnfilledTransactionSerializer(data=valid_serialized_data)

        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}


#
# class TestFilledTransactionSerializer:
#
#     def test_serialize_model(self, ftd):
#         t = baker.prepare(
#             'dogs.Transaction',
#             currency=baker.prepare('dogs.Currency')
#         )
#         expected_serialized_data = ftd(t)
#
#         serializer = FilledTransactionSerializer(t)
#
#         assert serializer.data == expected_serialized_data
#
#     def test_serialized_data(self):
#         t = FilledTransactionFactory.build()
#         valid_serialized_data = {
#             'id': t.id.hashid,
#             'name': t.name,
#             'currency': t.currency.code,
#             'creation_date': t.creation_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
#             'payment_date': t.payment_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
#             'stripe_response': t.stripe_response,
#             'payment_intent_id': t.payment_intent_id,
#             'billing_name': t.billing_name,
#             'billing_email': t.billing_email,
#             'payment_status': t.payment_status,
#             'link': t.link,
#             'email': t.email,
#             'amount_in_cents': t.amount_in_cents,
#             'message': t.message,
#         }
#
#         serializer = FilledTransactionSerializer(data=valid_serialized_data)
#
#         assert serializer.is_valid(raise_exception=True)
#         assert serializer.errors == {}
