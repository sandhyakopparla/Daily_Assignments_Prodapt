from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    spacialist=models.CharField(max_length=50)
    address=models.CharField(max_length=40)
    salary=models.IntegerField()