from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ReaderViewSet, AddressViewSet

router = SimpleRouter()
router.register("addresses", AddressViewSet, basename="addresses")
router.register("", ReaderViewSet, basename="readers")

urlpatterns = router.urls
