from rest_framework import serializers
from .models import Followers
from django.db import IntegrityError


class FollowersSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Followers
        fields = ['id', 'user', 'followed', 'created_at', 'followed_name']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'You have already followed this user.'})
