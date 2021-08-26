from rest_framework import serializers
from flat.models import Flat

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','building_no','owner_name','address','mbl_no','aadhar_no','email_id','password')