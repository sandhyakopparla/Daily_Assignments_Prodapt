from django.db import models

# Create your models here.
class Flatsapp(models.Model):
    buildingno=models.IntegerField()
    ownername=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    adhar=models.BigIntegerField()
    mobile=models.BigIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=20)
