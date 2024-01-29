from rest_framework import serializers
from .models import Followers
from django.db import IntegrityError

class FollowersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    follower_name = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Followers
        fields = ['id', 'user', 'follower', 'created_at', 'follower_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'You have already followed this user.'})