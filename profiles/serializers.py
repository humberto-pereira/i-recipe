from rest_framework import serializers
from .models import Profile
from followers.models import Followers

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_user(self, obj):
        request = self.context['request']
        return request.user == obj.user
    
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Followers.objects.filter(user=user, followed=obj.user).first()
            return following.id if following else None
    
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'name', 'content', 'image', 'is_user', 'following_id', 'posts_count', 'followers_count', 'following_count'
        ] # 'id' is created automatically by Django

