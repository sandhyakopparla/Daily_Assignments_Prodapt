from rest_framework import serializers
from flat.models import Flat
class flatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flat
        fields=("id","building_no","owner_name","mobile_no","address","adhar_no","emailId","password")

