from django.db.models import Avg
from rest_framework import serializers
from .models import RecipePosts
from likes.models import Like

class RecipePostsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    like_id = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
    
    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(user=user, post=obj).first()
            return like.id if like else None
        return None
    
    def get_average_rating(self, obj):
        average = obj.ratings.aggregate(average_rating=Avg('rating'))['average_rating'] or 0.0
        return round(average, 1) if average else None
    
    class Meta:
        model = RecipePosts
        fields = [
            'id', 'user', 'created_at', 'updated_at', 'title', 'content', 'profile_image', 'is_user', 'profile_id', 'image', 'tags', 'like_id', 'category', 'average_rating'
        ]

class RecipePostWithRatingSerializer(RecipePostsSerializer):
    avg_rating = serializers.SerializerMethodField()

    def get_avg_rating(self, obj):
        return obj.ratings.aggregate(Avg('rating')).get('rating__avg') or 0.0

    class Meta(RecipePostsSerializer.Meta):
        fields = RecipePostsSerializer.Meta.fields + ['avg_rating']
