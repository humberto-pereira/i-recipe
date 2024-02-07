from rest_framework import serializers
from .models import RecipeRating

class RecipeRatingSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    recipe_title = serializers.ReadOnlyField(source='recipe.title')
    average_rating = serializers.ReadOnlyField(source='recipe.average_rating')

    def get_is_user(self, obj):
        request = self.context.get('request')
        return request.user == obj.user
    
    class Meta:
        model = RecipeRating
        fields = ['id', 'recipe', 'user', 'rating', 'created_at', 'updated_at', 'profile_image', 'is_user', 'profile_id', 'recipe_title', 'average_rating']

class RecipeRatingDetailSerializer(RecipeRatingSerializer):
    """
    Serializer to represent the RecipeRating model so that it can be used for the detail view and don't need to repeat the code.
    """
    recipe = serializers.ReadOnlyField(source='post.id')