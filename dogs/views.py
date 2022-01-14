from rest_framework import viewsets
from .models import *
from .serializers import *


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UnfilledTransactionSerializer
        else:
            return FilledTransactionSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class OtherTransactionViewSet(viewsets.ModelViewSet):
    queryset = OtherTransaction.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UnfilledOtherTransactionSerializer
        else:
            return FilledOtherTransactionSerializer


class OtherCurrencyViewSet(viewsets.ModelViewSet):
    queryset = OtherCurrency.objects.all()
    serializer_class = OtherCurrencySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
