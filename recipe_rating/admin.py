from django.contrib import admin
from .models import RecipeRating
from django.db.models import Avg

@admin.register(RecipeRating)
class RecipeRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'user', 'rating', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('recipe__title', 'user__username')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _recipe_average_rating=Avg('recipe__ratings__rating')
        )
        return queryset

    def recipe_average_rating(self, obj):
        return obj._recipe_average_rating
    recipe_average_rating.admin_order_field = '_recipe_average_rating'
    recipe_average_rating.short_description = 'Recipe Average Rating'