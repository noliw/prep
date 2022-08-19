from unicodedata import name
from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)

    def __str__(self):
        return f"Dog named {self.name}"