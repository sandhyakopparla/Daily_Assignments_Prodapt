from rest_framework import serializers
from seller.models import Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sellername','address','phone_no','age')