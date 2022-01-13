from model_bakery import baker
import pytest


@pytest.fixture
def utbb():
    def unfilled_transaction_bakery_batch(n):
        utbb = baker.make(
            "dogs.Transaction",
            currency=baker.make("dogs.Currency"),
            _fill_optional=["name", "email", "currency", "message"],
            _quantity=n,
        )
        return utbb

    return unfilled_transaction_bakery_batch


@pytest.fixture
def ftbb():
    def filled_transaction_bakery_batch(n):
        ftbb = baker.make(
            "dogs.Transaction", currency=baker.make("dogs.Currency"), _quantity=n
        )
        return ftbb

    return filled_transaction_bakery_batch


@pytest.fixture
def ftb():
    def filled_transaction_bakery():
        ftb = baker.make("dogs.Transaction", currency=baker.make("dogs.Currency"))
        return ftb

    return filled_transaction_bakery


@pytest.fixture
def utbbnp():
    def unfilled_transaction_bakery_batch_not_persistent(n):
        utbb = baker.prepare(
            "dogs.Transaction",
            currency=baker.prepare("dogs.Currency"),
            _fill_optional=["name", "email", "currency", "message"],
            _quantity=n,
        )
        return utbb

    return unfilled_transaction_bakery_batch_not_persistent


@pytest.fixture
def ftbbnp():
    def filled_transaction_bakery_batch_not_persistent(n):
        ftbb = baker.prepare(
            "dogs.Transaction", currency=baker.prepare("dogs.Currency"), _quantity=n
        )
        return ftbb

    return filled_transaction_bakery_batch_not_persistent


@pytest.fixture
def ftbnp():
    def filled_transaction_bakery_not_persistent():
        ftb = baker.prepare("dogs.Transaction", currency=baker.prepare("dogs.Currency"))
        return ftb

    return filled_transaction_bakery_not_persistent
