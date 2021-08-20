from django.db import models
class Donar(models.Model):
    blood_group=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    last_donated_date=models.DateField()
# Create your models here.
