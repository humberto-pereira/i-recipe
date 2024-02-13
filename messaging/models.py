from django.db import models
from django.contrib.auth.models import User


class Conversation(models.Model):
    participants = models.ManyToManyField(User,
                                          related_name='conversations')


class Message(models.Model):
    conversation = models.ForeignKey(Conversation,
                                     related_name='messages',
                                     on_delete=models.CASCADE, null=True)
    sender = models.ForeignKey(User, related_name='sent_messages',
                               on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages',
                                  on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_edited = models.BooleanField(default=False)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.sender} to {
            self.recipient} sent on {self.created_at}"
