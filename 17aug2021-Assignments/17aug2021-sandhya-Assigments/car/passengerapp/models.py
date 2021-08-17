from django.db import models
class Passenger(models.Model):
    name=models.CharField(max_length=50)
    route=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    phono=models.CharField(max_length=50) 
# Create your models here.
