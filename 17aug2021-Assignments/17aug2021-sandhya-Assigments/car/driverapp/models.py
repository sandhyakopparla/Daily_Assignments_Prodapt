from django.db import models
class Driver(models.Model):
    name=models.CharField(max_length=50)
    carno=models.CharField(max_length=50)
    organisation=models.CharField(max_length=50)
    phono=models.CharField(max_length=50) 
# Create your models here.
