from django.contrib import admin
from .models import RecipePosts
from django.db.models import Avg

class RecipePostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'category_display', 'average_rating', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user', 'tags', 'category')
    search_fields = ('title', 'content', 'user__username', 'tags')

    def category_display(self, obj):
        return obj.category.name if obj.category else 'No Category'
    category_display.short_description = 'Category'

    def average_rating(self, obj):
        # Calculate the average rating for a recipe post
        avg_rating = obj.ratings.aggregate(average_rating=Avg('rating')).get('average_rating', 0.0)
        return round(avg_rating, 1) if avg_rating else 'Not Rated'
    average_rating.short_description = 'Average Rating'

    def get_queryset(self, request):
        # Annotate the queryset with an 'average_rating' field
        queryset = super().get_queryset(request).annotate(
            average_rating=Avg('ratings__rating')
        )
        return queryset

admin.site.register(RecipePosts, RecipePostsAdmin)