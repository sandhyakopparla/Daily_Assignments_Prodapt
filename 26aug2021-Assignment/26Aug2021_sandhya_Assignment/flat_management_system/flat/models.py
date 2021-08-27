from django.db import models
class Flat(models.Model):
    building_no=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    mobile_no=models.BigIntegerField()
    address=models.CharField(max_length=50)
    adhar_no=models.BigIntegerField()
    emailId=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    # id = models.AutoField(auto_created=True,primary_key=True,serialize=False)


    