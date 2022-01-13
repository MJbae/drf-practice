from rest_framework import serializers
from .models import Author, Book, Isbn


class IsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isbn
        fields = ("code",)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("name", "book_display_name", "isbn")


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name",)


class BookReportSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    isbn = IsbnSerializer(read_only=True)
    book_display_name = serializers.SerializerMethodField(
        source="get_book_display_name"
    )

    def get_book_display_name(self, book):
        return book.name.upper()

    class Meta:
        model = Book
        fields = ("name", "book_display_name", "isbn", "author")
