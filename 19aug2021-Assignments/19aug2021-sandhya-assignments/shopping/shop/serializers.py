from rest_framework import serializers
from shop.models import Shop
class shopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop 
        fields=("shop_name","address","emailid","website","phono","username","password","confirm_password")