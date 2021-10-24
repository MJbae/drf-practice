from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    book_display_name = serializers.SerializerMethodField(source='get_book_display_name')

    def get_book_display_name(self, book):
        return book.name.upper()

    class Meta:
        model = Book
        fields = "__all__"
