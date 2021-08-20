from rest_framework import serializers
from donar.models import Donar
class donarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donar 
        fields=("blood_group","name","address","pincode","mobileno","last_donated_date")