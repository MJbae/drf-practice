from django.db import models


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


class Owner(models.Model):
    name = models.CharField(max_length=64, null=True)
    dog_set = models.ManyToManyField(Dog, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)
    dog_set = models.ManyToManyField(Dog, blank=True)
