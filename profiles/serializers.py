from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
    
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'name', 'content', 'image', 'is_user'
        ] # 'id' is created automatically by Django

