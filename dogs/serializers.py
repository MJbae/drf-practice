from rest_framework import serializers
from .models import *



class DogSerializer(serializers.ModelSerializer):
    # owners = OwnerSerializer(many=True)
    # customers = CustomerSerializer(many=True)

    class Meta:
        model = Dog
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        
        
class CustomerSerializer(serializers.ModelSerializer):
    dogs = DogSerializer(many=True, source='dog_set')

    class Meta:
        model = Customer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    dogs = DogSerializer(many=True, source='dog_set')

    class Meta:
        model = Owner

