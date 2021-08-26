from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Villa(models.Model):
    Name = CharField(max_length=50)
    Address = CharField(max_length=50)
    Phn_no = CharField(max_length=50)
    Email_id =CharField(max_length=50)
    package = CharField(max_length=50,default=False)
    