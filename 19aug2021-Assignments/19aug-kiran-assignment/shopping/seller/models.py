from django.db import models

# Create your models here.
class Seller(models.Model):
    sellername=models.CharField(max_length=50)
    address=models.CharField(max_length=30)
    phone_no=models.BigIntegerField()
    age=models.IntegerField()