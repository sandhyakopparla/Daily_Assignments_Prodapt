from rest_framework import serializers
from seller.models import Seller
class sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Seller 
        fields=("seller_name","address","emailid","phono","date_of_birth","district","age","adharno")
        