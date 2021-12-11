from rest_framework.test import APIClient
from model_bakery import baker
import pytest


@pytest.fixture
def utbb():
    def unfilled_transaction_bakery_batch(n):
        utbb = baker.make(
            'dogs.Transaction',
            _fill_optional=[
                'name',
                'email',
                'currency',
                'message'
            ],
            currency=baker.make('dogs.Currency'),
            _quantity=n
        )
        return utbb

    return unfilled_transaction_bakery_batch


@pytest.fixture
def ftbb():
    def filled_transaction_bakery_batch(n):
        utbb = baker.make(
            'dogs.Transaction',
            _quantity=n
        )
        return utbb

    return filled_transaction_bakery_batch


@pytest.fixture
def ftb():
    def filled_transaction_bakery():
        utbb = baker.make(
            'dogs.Transaction',
            currency=baker.make('dogs.Currency')
        )
        return utbb

    return filled_transaction_bakery
