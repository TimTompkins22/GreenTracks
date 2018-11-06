from django.db import models


# Create your models here.


class Entry(models.Model):
    id = models.IntegerField()
    supplier = models.CharField(max_length=50)
    product = models.CharField(max_length=25)
    price = models.IntegerField()

