from django.db import models
from django.db.models.fields import BigIntegerField, CharField, IntegerField

# Create your models here.
class Flatsmanage(models.Model):
    Building_no = IntegerField()
    Owner_name = CharField(max_length=50)
    Address = CharField(max_length=50)
    Mob_no = CharField(max_length=50)
    Adhar_no = CharField(max_length=50)
    email_id = CharField(max_length=50)
    password = CharField(max_length=10)
