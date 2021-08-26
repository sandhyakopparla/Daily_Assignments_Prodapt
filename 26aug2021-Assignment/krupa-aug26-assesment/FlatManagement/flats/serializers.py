from rest_framework import serializers
from flats.models import Flat

class flatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','buildingno','ownername','address','mobileno','email','adharno','password')