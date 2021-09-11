from rest_framework import serializers
from .models import Kit

class KitSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'headline', 'distance', 'note', 'created_at', 'update_at')
        model = Kit
