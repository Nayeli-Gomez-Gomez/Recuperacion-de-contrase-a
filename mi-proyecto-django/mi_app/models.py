from django.db import models

# Create your models here.

class product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.IntegerField()
    count = models.IntegerField()