from rest_framework import serializers
from .models import RecipePosts
from likes.models import Like

class RecipePostsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    like_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError('Image size should be up to 2MB.')
        if value.image.width > 4096:
            raise serializers.ValidationError('Image width should be up to 4096px.')
        if value.image.height > 4096:
            raise serializers.ValidationError('Image height should be up to 4096px.')
        return value

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(user=user, post=obj).first()
            return like.id if like else None
        return None
    
    class Meta:
        model = RecipePosts
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'title', 'content', 'profile_image', 'is_user', 'profile_id', 'image', 'tags', 'like_id', 'category'
        ] # 'id' is created automatically by Django