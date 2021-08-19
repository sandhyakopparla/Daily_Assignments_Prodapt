from django.db import models
class Product(models.Model):
    productname=models.CharField(max_length=50)
    productdetails=models.CharField(max_length=50)
    sellername=models.CharField(max_length=50)
    manufacturer_name=models.CharField(max_length=50) 
    manufacturing_date=models.CharField(max_length=50) 
    price=models.CharField(max_length=50)
# Create your models here.
