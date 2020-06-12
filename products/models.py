from django.db import models


class Products (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    price = models.FloatField()
    code = models.CharField(max_length= 255)
    description = models.CharField(max_length=2083)
    discount = models.FloatField(0.2)
