from django.db import models

# Create your models here.
class Flat(models.Model):
    building_no=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=50)
    aadhar_no=models.CharField(max_length=50)
    mail_id=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

