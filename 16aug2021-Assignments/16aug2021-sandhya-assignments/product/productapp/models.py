from django.db import models
class Product(models.Model):
    code=models.IntegerField()
    name = models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    price=models.IntegerField()
# Create your models here.
