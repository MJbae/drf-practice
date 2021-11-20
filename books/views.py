from rest_framework import viewsets
from .models import Author, Book, Isbn
from .serializers import AuthorSerializer, BookSerializer, IsbnSerializer, BookReportSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    # def get_queryset(self):
    #     queryset = Book.objects.prefetch_related('author').all()
    #     print(f'queryset: {queryset.query}')
    #     return queryset


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookReportViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookReportSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        print(f'queryset: {queryset.query}')
        return queryset


class IsbnViewSet(viewsets.ModelViewSet):
    queryset = Isbn.objects.all()
    serializer_class = IsbnSerializer

    def get_queryset(self):
        queryset = Isbn.objects.prefetch_related('book').all()
        print(f'queryset: {queryset.query}')
        return queryset
