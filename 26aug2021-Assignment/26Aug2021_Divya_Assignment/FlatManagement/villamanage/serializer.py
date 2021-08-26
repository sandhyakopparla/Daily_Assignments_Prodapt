from django.db.models import fields
from rest_framework import serializers
from villamanage.models import Villa

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Villa
        fields = ("Name","Address","Phn_no","Email_id","package")