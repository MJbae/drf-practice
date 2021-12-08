import inspect
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .models import Reader, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ReaderSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ('id', 'name', 'email', 'addresses', 'latest_city')
