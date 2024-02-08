from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import RecipeComments

class RecipeCommentsSerializer(serializers.ModelSerializer):
    """
    Serializer to represent the RecipeComments model.
    """
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    class Meta:
        model = RecipeComments
        fields = [
            'id', 'user', 'post', 'created_at', 'updated_at', 'content', 'profile_image', 'is_user', 'profile_id', 
        ] # 'id' is created automatically by Django

class RecipeCommentsDetailSerializer(RecipeCommentsSerializer):
    """
    Serializer to represent the RecipeComments model so that it can be used for the detail view and don't need to repeat the code.
    """
    post = serializers.ReadOnlyField(source='post.id')