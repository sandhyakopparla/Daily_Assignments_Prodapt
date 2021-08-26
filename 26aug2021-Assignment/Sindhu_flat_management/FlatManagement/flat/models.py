from django.db import models

# Create your models here.
class Flat(models.Model):
    buildingno=models.IntegerField()
    ownername=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mobileno=models.BigIntegerField()
    adhaarno=models.IntegerField()
    emailid=models.CharField(max_length=50) 
    password=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
