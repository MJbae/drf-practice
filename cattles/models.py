from django.db import models


# class to define choices
class SexCategory(models.TextChoices):
    COW = 'C'
    OX = 'O'
    BULL = 'B'


class PublicCattle(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    birth_date = models.DateField
    sex = models.CharField(
        max_length=1,
        choices=SexCategory.choices,
    )
