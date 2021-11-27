import inspect
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from .models import Reader, Address


class BulkListSerializer(serializers.ListSerializer):
    def update(self, queryset, validated_data):
        id_attr = getattr(self.child.Meta, 'update_lookup_field')
        update_data = {i.get(id_attr): i for i in validated_data}

        if not all((bool(i) and not inspect.isclass(i) for i in update_data.keys())):
            raise NotFound(_('Could not find all objects to update'))

        objects = queryset.filter(**{'{}__in'.format(id_attr): update_data.keys()})

        if len(update_data) != objects.count():
            raise NotFound(_('Could not find all objects to update'))

        response = []
        for id, data in update_data.items():
            for obj in objects:
                if str(getattr(obj, id_attr)) == str(id):
                    response.append(self.child.update(obj, data))

        return response


class AddressSerializer(serializers.ModelSerializer):
    address_pk = serializers.IntegerField()

    class Meta:
        model = Address
        fields = '__all__'
        update_lookup_field = 'address_pk'
        list_serializer_class = BulkListSerializer


class ReaderSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = ('id', 'name', 'email', 'addresses', 'latest_city')
