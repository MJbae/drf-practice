from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import DogViewSet

router = SimpleRouter()
router.register(r'transactions', DogViewSet, basename='transactions')
router.register(r'currencies', DogViewSet, basename='currencies')
router.register(r'', DogViewSet, basename='dogs')

urlpatterns = router.urls

