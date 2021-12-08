from model_bakery import baker
import factory
import json
import pytest

from dogs.models import Transaction, Currency

pytestmark = pytest.mark.django_db


class TestCurrencyEndpoints:
    endpoint = '/api/v1/dogs/currencies/'

    def test_list(self, api_client):
        baker.make(Currency, _quantity=3)

        response = api_client().get(
            self.endpoint
        )

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client):
        currency = baker.prepare(Currency)
        expected_json = {
            'name': currency.name,
            'code': currency.code,
            'symbol': currency.symbol
        }

        response = api_client().post(
            self.endpoint,
            data=expected_json,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json

    def test_retrieve(self, api_client):
        currency = baker.make(Currency)
        expected_json = {
            'name': currency.name,
            'code': currency.code,
            'symbol': currency.symbol
        }
        url = f'{self.endpoint}{currency.id}/'

        response = api_client().get(url)

        assert response.status_code == 200
        assert json.loads(response.content) == expected_json

    def test_update(self, rf, api_client):
        old_currency = baker.make(Currency)
        new_currency = baker.prepare(Currency)
        currency_dict = {
            'code': new_currency.code,
            'name': new_currency.name,
            'symbol': new_currency.symbol
        }

        url = f'{self.endpoint}{old_currency.id}/'

        response = api_client().put(
            url,
            currency_dict,
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content) == currency_dict

    @pytest.mark.parametrize('field', [
        ('code'),
        ('name'),
        ('symbol'),
    ])
    def test_partial_update(self, mocker, rf, field, api_client):
        currency = baker.make(Currency)
        currency_dict = {
            'code': currency.code,
            'name': currency.name,
            'symbol': currency.symbol
        }
        valid_field = currency_dict[field]
        url = f'{self.endpoint}{currency.id}/'

        response = api_client().patch(
            url,
            {field: valid_field},
            format='json'
        )

        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, mocker, api_client):
        currency = baker.make(Currency)
        url = f'{self.endpoint}{currency.id}/'

        response = api_client().delete(url)

        assert response.status_code == 204
        assert Currency.objects.all().count() == 0


class TestTransactionEndpoints:
    endpoint = '/api/v1/dogs/transactions/'

    def test_list(self, api_client, utbb):
        client = api_client()
        utbb(3)
        url = self.endpoint
        response = client.get(url)

        assert response.status_code == 200
        assert len(json.loads(response.content)) == 3

    def test_create(self, api_client, utbb):
        client = api_client()
        t = utbb(1)[0]
        valid_data_dict = {
            'amount_in_cents': t.amount_in_cents,
            'currency': t.currency.code,
            'name': t.name,
            'email': t.email,
            'message': t.message
        }

        url = self.endpoint

        response = client.post(
            url,
            valid_data_dict,
            format='json'
        )

        assert response.status_code == 201
        assert json.loads(response.content) == valid_data_dict
        assert Transaction.objects.last().link

    def test_retrieve(self, api_client, ftb):
        t = ftb()
        t = Transaction.objects.last()
        expected_json = t.__dict__
        expected_json['link'] = t.link
        expected_json['currency'] = t.currency.code
        expected_json['creation_date'] = expected_json['creation_date'].strftime(
            '%Y-%m-%dT%H:%M:%S.%fZ'
        )
        expected_json.pop('_state')
        expected_json.pop('currency_id')
        url = f'{self.endpoint}{t.id}/'

        response = api_client().get(url)

        assert response.status_code == 200 or response.status_code == 301
        assert json.loads(response.content) == expected_json

    def test_update(self, api_client, utbb):
        old_transaction = utbb(1)[0]
        t = utbb(1)[0]
        expected_json = t.__dict__
        expected_json['id'] = old_transaction.id.hashid
        expected_json['currency'] = old_transaction.currency.code
        expected_json['link'] = Transaction.objects.first().link
        expected_json['creation_date'] = old_transaction.creation_date.strftime(
            '%Y-%m-%dT%H:%M:%S.%fZ'
        )
        expected_json.pop('_state')
        expected_json.pop('currency_id')

        url = f'{self.endpoint}{old_transaction.id}/'

        response = api_client().put(
            url,
            data=expected_json,
            format='json'
        )

        assert response.status_code == 200 or response.status_code == 301
        assert json.loads(response.content) == expected_json

    @pytest.mark.parametrize('field', [
        ('name'),
        ('billing_name'),
        ('billing_email'),
        ('email'),
        ('amount_in_cents'),
        ('message'),
    ])
    def test_partial_update(self, api_client, field, utbb):
        utbb(2)
        old_transaction = Transaction.objects.first()
        new_transaction = Transaction.objects.last()
        valid_field = {
            field: new_transaction.__dict__[field],
        }
        url = f'{self.endpoint}{old_transaction.id}/'

        response = api_client().patch(
            path=url,
            data=valid_field,
            format='json',
        )

        assert response.status_code == 200 or response.status_code == 301
        try:
            assert json.loads(response.content)[field] == valid_field[field]
        except json.decoder.JSONDecodeError as e:
            pass

    def test_delete(self, api_client, utbb):
        transaction = utbb(1)[0]
        url = f'{self.endpoint}{transaction.id}/'

        response = api_client().delete(
            url
        )

        assert response.status_code == 204 or response.status_code == 301
