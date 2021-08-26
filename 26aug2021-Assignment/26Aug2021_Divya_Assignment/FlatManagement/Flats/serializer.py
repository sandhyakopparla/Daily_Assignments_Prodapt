from django.db.models import fields
from rest_framework import serializers
from Flats.models import Flatsmanage

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flatsmanage
        fields = ("id","Building_no","Owner_name","Address","Mob_no","Adhar_no","email_id","password")