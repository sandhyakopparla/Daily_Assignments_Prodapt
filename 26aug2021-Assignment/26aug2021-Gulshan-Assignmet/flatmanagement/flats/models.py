from django.db import models
from django.db.models.fields import BigIntegerField, EmailField

# Create your models here.

class Flats(models.Model):
    bulding_no = models.IntegerField()
    owner_name = models.CharField(max_length=300)
    address = models.CharField(max_length=2000)
    mobile_no =models.BigIntegerField()
    adhar_no = models.BigIntegerField()
    emailid = models.EmailField()
    password = models.CharField(max_length=200)
    id = models.AutoField(auto_created=True,primary_key=True,serialize=False)

