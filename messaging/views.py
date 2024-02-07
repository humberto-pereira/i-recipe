from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from django.utils import timezone
from datetime import timedelta
from i_recipe_api.permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import PermissionDenied

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
        obj = super().get_object()
        # Allow both sender and recipient to read the message
        # Only raise PermissionDenied if a non-sender tries to update or delete
        if self.request.method == 'GET' and obj.recipient == self.request.user and not obj.read:
            obj.read = True
            obj.save()
        elif self.request.method in ['PUT', 'PATCH', 'DELETE'] and obj.sender != self.request.user:
            raise PermissionDenied("You do not have permission to modify or delete this message.")
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