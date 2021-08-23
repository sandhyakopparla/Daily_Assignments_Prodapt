from rest_framework import serializers
from cricket.models import Cricket
class cricketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cricket
        fields=("cricketer_name","matchone_score","matchtwo_score","location","team","batting_style","bowling_style")
