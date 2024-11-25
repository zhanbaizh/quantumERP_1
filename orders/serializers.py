from rest_framework import serializers
from .models import Order, TechCard, InventoryItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class TechCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCard
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
