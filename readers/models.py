from django.db import models


class Reader(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()


class Address(models.Model):
    detail = models.CharField(max_length=100)
    city = models.FloatField()
    reader = models.ForeignKey(Reader, related_name="addresses", on_delete=models.CASCADE)
