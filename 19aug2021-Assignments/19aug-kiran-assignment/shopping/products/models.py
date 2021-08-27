from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=50)
    productdetails=models.CharField(max_length=30)
    sellername=models.CharField(max_length=50)
    price=models.IntegerField()