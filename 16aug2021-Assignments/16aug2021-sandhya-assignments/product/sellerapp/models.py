from django.db import models
class Seller(models.Model):
    sellerid=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phono=models.CharField(max_length=50) 
