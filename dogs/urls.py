from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register(r'transactions', TransactionViewSet, basename='transactions')
router.register(r'currencies', CurrencyViewSet, basename='currencies')
router.register(r'', DogViewSet, basename='dogs')

urlpatterns = router.urls

