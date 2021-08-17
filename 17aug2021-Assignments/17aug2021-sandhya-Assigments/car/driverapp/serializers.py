from rest_framework import serializers
from driverapp.models import Driver
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver 
        fields=("name","carno","organisation","phono")
