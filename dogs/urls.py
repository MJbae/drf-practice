from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DogViewSet, CustomerViewSet, OwnerViewSet

router = SimpleRouter()
router.register('customers', CustomerViewSet, basename='customer')
router.register('owners', OwnerViewSet, basename='owner')
router.register('', DogViewSet, basename='dog')

urlpatterns = router.urls
