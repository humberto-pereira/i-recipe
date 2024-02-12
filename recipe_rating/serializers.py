from rest_framework import serializers
from .models import RecipeRating

class RecipeRatingSerializer(serializers.ModelSerializer):

    your_rating = serializers.ChoiceField(choices=RecipeRating.rating.field.choices, source='rating')
    recipe_average_rating = serializers.SerializerMethodField()
    user = serializers.ReadOnlyField(source='user.username')
    is_user = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='user.profile.id')
    profile_image = serializers.ReadOnlyField(source='user.profile.image.url')
    recipe_title = serializers.ReadOnlyField(source='recipe.title')
    

    def get_is_user(self, obj):
        """
        Check if the request's user is the object's user, ensuring object is saved and request is authenticated.
        """
        request = self.context.get('request')
        if hasattr(obj, 'pk') and request and hasattr(request, "user"):
            return obj.user == request.user
        return False


    class Meta:
        model = RecipeRating
        fields = ['id', 'recipe', 'user', 'created_at', 'updated_at', 'profile_image', 'is_user', 'profile_id', 'recipe_title', 'your_rating','recipe_average_rating']

    def get_recipe_average_rating(self, obj):
        return RecipeRating.calculate_average_for_recipe(obj.recipe_id)

class RecipeRatingDetailSerializer(RecipeRatingSerializer):
    """
    Serializer to represent the RecipeRating model so that it can be used for the detail view and don't need to repeat the code.
    """
    recipe = serializers.ReadOnlyField(source='post.id')