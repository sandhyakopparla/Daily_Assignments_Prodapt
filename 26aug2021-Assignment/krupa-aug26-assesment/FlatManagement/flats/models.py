from django.db import models

# Create your models here.
class Flat(models.Model):
    buildingno=models.BigIntegerField()
    ownername=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    email=models.CharField(max_length=50)
    adharno=models.BigIntegerField()
    password=models.BigIntegerField()


