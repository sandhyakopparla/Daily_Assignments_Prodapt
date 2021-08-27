from django.db import models

# Create your models here.
class Shop(models.Model):
    shopname=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    phone_number=models.BigIntegerField()
    