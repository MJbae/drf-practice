from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DogViewSet

router = SimpleRouter()
router.register('', DogViewSet, basename='dogs')

urlpatterns = router.urls
