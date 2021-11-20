from django.db import models


class Sex(models.TextChoices):
    Female = 'F'
    Male = 'M'


class Dog(models.Model):
    birth_date = models.DateField(null=True)
    sex = models.CharField(
        max_length=1,
        choices=Sex.choices,
    )