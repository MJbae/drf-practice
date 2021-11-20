from rest_framework import viewsets
from .models import Dog
from .serializers import DogSerializer


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

