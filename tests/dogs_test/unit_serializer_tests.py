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


class TestCurrencyViewSet:

    def test_list(self, mocker, rf):
        # Arrange
        url = reverse('currencies-list')
        request = rf.get(url)
        qs = MockSet(
            baker.prepare(Currency),
            baker.prepare(Currency),
            baker.prepare(Currency)
        )
        view = CurrencyViewSet.as_view(
            {'get': 'list'}
        )
        # Mcking
        mocker.patch.object(
            CurrencyViewSet, 'get_queryset', return_value=qs
        )
        # Act
        response = view(request).render()
        # Assert
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_retrieve(self, mocker, rf):
        currency = baker.prepare(Currency)
        expected_json = {
            'name': currency.name,
            'code': currency.code,
            'symbol': currency.symbol
        }
        url = reverse('currencies-detail', kwargs={'pk': currency.id})
        request = rf.get(url)
        mocker.patch.object(
            CurrencyViewSet, 'get_queryset', return_value=MockSet(currency)
        )
        view = CurrencyViewSet.as_view(
            {'get': 'retrieve'}
        )

        response = view(request, pk=currency.id).render()
        response_body = json.loads(response.content)
        del (response_body['id'])

        assert response.status_code == 200
        assert response_body == expected_json
