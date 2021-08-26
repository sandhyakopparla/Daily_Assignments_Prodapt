from rest_framework import serializers
from flat.models import Flat

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=('id','buildingno','ownername','address','mobileno','adhaarno','emailid','password')