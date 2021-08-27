from django.db.models.base import Model
from flats.models import Flats
from rest_framework import fields, serializers

class FlatsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Flats
        fields = ("id","bulding_no","owner_name","address","mobile_no","adhar_no","emailid","password")