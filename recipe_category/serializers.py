from rest_framework import serializers
from .models import Category
from recipe_posts.serializers import RecipePostsSerializer


class CategorySerializer(serializers.ModelSerializer):
    recipe_posts = RecipePostsSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'recipe_posts']
