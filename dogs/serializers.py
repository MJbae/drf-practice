from rest_framework import serializers
from .models import Dog, Customer, Owner


class CustomerSerializer(serializers.ModelSerializer):
    # dog_set = DogSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    # dog_set = DogSerializer(read_only=True)

    class Meta:
        model = Owner
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    owners = OwnerSerializer(many=True)
    customers = CustomerSerializer(many=True)

    class Meta:
        model = Dog
        fields = "__all__"
