from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import AuthorViewSet, BookViewSet, BookReportViewSet

router = SimpleRouter()
router.register("authors", AuthorViewSet, basename="authors")
router.register("", BookReportViewSet, basename="books")

urlpatterns = router.urls
