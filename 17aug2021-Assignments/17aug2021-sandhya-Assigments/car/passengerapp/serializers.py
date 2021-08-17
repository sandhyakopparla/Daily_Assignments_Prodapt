from rest_framework import serializers
from passengerapp.models import Passenger
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields=("name","route","address","phono")
