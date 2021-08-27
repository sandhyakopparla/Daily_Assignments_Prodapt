from Flats.models import flat
from django.db.models import fields
from rest_framework import serializers

class flatSerializer(serializers.ModelSerializer):
    class Meta:
        model = flat
        fields = ("flatno","buildingno","ownerName","address","mobile","aadhar","email", "password")

        
