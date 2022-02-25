from tabnanny import verbose
from django.db import models
from turtle import title
# Create your models here.

class prediction(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    year = models.IntegerField(max_length=50, verbose_name="year")
    present_price = models.IntegerField(max_length=50, verbose_name="present price")
    driven_km = models.IntegerField(max_length=50, verbose_name="driven km")
    fuel_type = models.CharField(max_length=50, verbose_name="fuel type")
    seller_type = models.CharField(max_length=50, verbose_name="seller type")
    transmission_type = models.CharField(max_length=50, verbose_name="transmission type")

    def __str__(self) -> str:
        return self.title

class output(models.Model):
    title = models.CharField(max_length=50, verbose_name="title")
    value = models.CharField(max_length=50, verbose_name="value")

    def __str__(self) -> str:
        return self.title