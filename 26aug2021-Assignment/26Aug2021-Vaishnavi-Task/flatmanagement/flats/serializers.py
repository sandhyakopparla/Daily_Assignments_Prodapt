from django.db import models
from flats.models import Flatsapp
from rest_framework import serializers
from django.db.models import fields

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flatsapp
        fields=('buildingno','ownername','address','adhar','mobile','email','password')