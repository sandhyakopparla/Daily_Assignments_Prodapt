from django.db import models
class Seller(models.Model):
    seller_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    phono=models.BigIntegerField()
    date_of_birth=models.CharField(max_length=50) 
    district=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    adharno=models.CharField(max_length=50)


# Create your models here.
