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
