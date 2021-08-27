from django.db import models

# Create your models here.
class Donor(models.Model):
    name=models.CharField(max_length=30)
    blood_group=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    mobile_no=models.BigIntegerField()
    last_Donated_date=models.DateField()