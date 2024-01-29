from django.db import IntegrityError
from rest_framework import serializers
from .models import Like

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model=Like
        fields = ['id', 'user', 'post', 'created_at']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'You have already liked this post.'})