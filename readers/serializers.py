from rest_framework import serializers
from .models import Reader, Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'detail', 'city', 'reader')


class ReaderSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ('id', 'name', 'email', 'addresses')
