from django.db import models

from config import settings


class Sex(models.TextChoices):
    Female = 'F'
    Male = 'M'


class Dog(models.Model):
    name = models.CharField(max_length=64, null=True)
    birth_date = models.DateField(null=True)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
    )


import string
from django.db import models
from django.utils import timezone
from hashid_field import HashidAutoField


class Currency(models.Model):
    """Currency model"""
    name = models.CharField(max_length=120, null=False, blank=False, unique=True)
    code = models.CharField(max_length=3, null=False, blank=False, unique=True)
    symbol = models.CharField(max_length=5, null=False, blank=False, default='$')

    def __str__(self) -> str:
        return self.code


class Transaction(models.Model):
    """Transaction model."""
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    creation_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    currency = models.ForeignKey(Currency, null=False, blank=False, default=1, on_delete=models.PROTECT)
    payment_status = models.CharField(max_length=21, null=True)
    payment_intent_id = models.CharField(max_length=100, null=True, blank=False, default=None)
    message = models.TextField(null=True, blank=True)


class Owner(models.Model):
    name = models.CharField(max_length=64, null=True)
    dog_set = models.ManyToManyField(Dog, blank=True, related_name="owners")


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)
    dog_set = models.ManyToManyField(Dog, blank=True, related_name="customers")
