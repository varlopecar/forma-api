from rest_framework import serializers
from forma.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']