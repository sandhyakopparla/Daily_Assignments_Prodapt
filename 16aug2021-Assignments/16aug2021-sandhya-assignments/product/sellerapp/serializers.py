from rest_framework import serializers
from sellerapp.models import Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields=('sellerid','name','address','phono')