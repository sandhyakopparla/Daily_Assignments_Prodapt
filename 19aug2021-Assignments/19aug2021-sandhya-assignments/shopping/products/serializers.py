from rest_framework import serializers
from products.models import Product 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=("productname","productdetails","sellername","manufacturer_name","manufacturing_date","price")
