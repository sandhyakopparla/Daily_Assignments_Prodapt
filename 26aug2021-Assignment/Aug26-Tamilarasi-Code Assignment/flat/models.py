from django.db import models

# Create your models here.
class Flat(models.Model):
    building_no=models.IntegerField()
    owner_name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    mbl_no=models.BigIntegerField()
    aadhar_no=models.BigIntegerField()
    email_id=models.EmailField()
    password=models.CharField(max_length=50)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    