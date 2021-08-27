from rest_framework import serializers
from donors.models import Donor
class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=('name','blood_group','address','pincode','mobile_no','last_Donated_date')
