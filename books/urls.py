from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet

router = SimpleRouter()
router.register('authors', AuthorViewSet, basename='authors')
router.register('', BookViewSet, basename='books')

urlpatterns = router.urls
