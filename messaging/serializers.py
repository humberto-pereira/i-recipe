from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message, Conversation
from django.db.models import Q, Count


class MessageSerializer(serializers.ModelSerializer):
    message_id = serializers.IntegerField(source='id', read_only=True)
    sender_username = serializers.ReadOnlyField(source='sender.username')
    recipient_username = serializers.ReadOnlyField(source='recipient.username')
    sender_profile_image = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Message
        fields = [
                'message_id', 'sender', 'sender_username', 'recipient',
                'recipient_username', 'body', 'created_at', 'updated_at',
                'read', 'sender_profile_image', 'conversation'
        ]
        read_only_fields = ('sender', 'created_at', 'updated_at',
                            'read', 'conversation')

    def get_sender_username(self, obj):
        return obj.sender.username

    def get_recipient_username(self, obj):
        return obj.recipient.username

    def get_sender_profile_image(self, obj):
        if hasattr(obj.sender, 'profile') and obj.sender.profile.image:
            return obj.sender.profile.image.url
        return None

    def create(self, validated_data):
        sender = self.context['request'].user
        recipient = validated_data['recipient']

        # Check if a conversation between these users already exists,
        # considering both directions
        conversation = Conversation.objects.annotate(
            total_participants=Count('participants')
        ).filter(
            Q(participants=sender) & Q(participants=recipient)
            & Q(total_participants=2)
        ).distinct().first()

        if not conversation:
            # Create a new conversation if none exists
            conversation = Conversation.objects.create()
            conversation.participants.add(sender, recipient)

        validated_data['sender'] = sender
        validated_data['conversation'] = conversation
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Prevent updating certain fields if necessary
        For example, to prevent changing the sender or recipient
        """
        validated_data.pop('sender', None)
        validated_data.pop('recipient', None)

        return super().update(instance, validated_data)


class ConversationSerializer(serializers.ModelSerializer):
    conversation_id = serializers.IntegerField(source='id', read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages']
