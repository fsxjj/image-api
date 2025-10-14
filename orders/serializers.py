from rest_framework import serializers
from .models import WallPaintingOrder

class WallPaintingOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WallPaintingOrder
        fields = '__all__'
