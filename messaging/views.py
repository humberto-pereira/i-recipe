from django.db.models import Q
from rest_framework import generics, permissions
from .models import Message, Conversation
from .serializers import MessageSerializer, ConversationSerializer
from django.utils import timezone
from datetime import timedelta
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.views import status

class MessageListView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(recipient=user).order_by('-created_at')
    
    

class MessageDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # This queryset allows both senders and recipients to access messages.
        return Message.objects.filter(Q(sender=user) | Q(recipient=user))

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        obj = queryset.filter(**filter_kwargs).first()
        if not obj:
            # Custom message for not found
            raise NotFound(detail="Message does not exist or you do not have permission to view it.", code=status.HTTP_404_NOT_FOUND)

        # Perform permission checks for update/delete actions
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            if obj.sender != self.request.user:
                raise PermissionDenied("You do not have permission to modify or delete this message.")
        elif self.request.method == 'GET' and obj.recipient == self.request.user and not obj.read:
            obj.read = True
            obj.save()

        return obj

    def perform_update(self, serializer):
        # Check if the message can be edited (within 24 hours)
        if timezone.now() - serializer.instance.created_at > timedelta(hours=24):
            raise PermissionDenied("Messages can only be edited within 24 hours of sending.")
        serializer.save(is_edited=True)

    def perform_destroy(self, instance):
        # Check if the message can be deleted based on your logic (e.g., within 24 hours)
        if timezone.now() - instance.created_at > timedelta(hours=24):
            raise PermissionDenied("Messages can only be deleted within 24 hours of sending.")
        instance.delete()

class ConversationListView(generics.ListAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can access this view

    def get_queryset(self):
        # Ensure only authenticated users can see their conversations
        user = self.request.user
        return Conversation.objects.filter(participants__in=[user]).distinct()

    def get_queryset(self):
        # Check if the user is authenticated
        user = self.request.user
        if user.is_authenticated:
            # Filter conversations to only those where the current user is a participant
            return Conversation.objects.filter(participants__in=[user]).distinct()
        else:
            # Optionally handle unauthenticated users, such as returning an empty queryset
            return Conversation.objects.all()

class ConversationDetailView(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Retrieve the conversation object
        conversation = super().get_object()
        user = self.request.user
        if user not in conversation.participants.all():
            raise PermissionDenied("You do not have permission to view this conversation.")
        return conversation