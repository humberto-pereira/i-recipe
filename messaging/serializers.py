from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')
    sender_profile_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'recipient', 'recipient_username', 'body', 'created_at', 'read', 'sender_profile_image']
        read_only_fields = ('sender', 'created_at', 'read')

    def get_sender_username(self, obj):
        return obj.sender.username

    def get_recipient_username(self, obj):
        return obj.recipient.username

    def get_sender_profile_image(self, obj):
        if hasattr(obj.sender, 'profile') and obj.sender.profile.image:
            return obj.sender.profile.image.url
        return None

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['sender'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """ 
        Prevent updating certain fields if necessary
        For example, to prevent changing the sender or recipient
        """
        validated_data.pop('sender', None)
        validated_data.pop('recipient', None)
        
        return super().update(instance, validated_data)
