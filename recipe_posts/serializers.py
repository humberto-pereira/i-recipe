from rest_framework import serializers
from .models import Post

class RecipePostsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')

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
    
    class Meta:
        model = Post
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'title', 'content', 'image', 'is_user', 'profile_id', 'image'
        ] # 'id' is created automatically by Django