from django.db import models

# Create your models here.
class flat(models.Model):
    flatno = models.IntegerField(default='')
    buildingno = models.IntegerField(default ='')
    ownerName = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    mobile = models.BigIntegerField(default='')
    aadhar = models.BigIntegerField(default='')
    email = models.CharField(max_length=50, default='')
    password =models.CharField(max_length=50, default='')

    