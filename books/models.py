from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)


class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey("Author", models.CASCADE, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
