from django.db import models
class Shop(models.Model):
    shop_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    emailid=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    phono=models.BigIntegerField()
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

# Create your models here.
