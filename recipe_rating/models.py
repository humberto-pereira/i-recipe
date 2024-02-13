from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from recipe_posts.models import RecipePosts


class RecipeRating(models.Model):
    recipe = models.ForeignKey(RecipePosts, on_delete=models.CASCADE,
                               related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-rating']
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"""{self.user.username}'s rating of
                   {self.recipe.title}: {self.rating}"""

    @staticmethod
    def calculate_average_for_recipe(recipe_id):
        """
        Calculates the average rating for a given recipe,
        rounded to the nearest 0.5
        """
        average_rating = ((RecipeRating.objects.filter
                          (recipe_id=recipe_id).aggregate
                          (Avg('rating'))['rating__avg']))
        if average_rating is not None:
            # Round to the nearest 0.5
            return round(average_rating * 2) / 2
        return 0.0
