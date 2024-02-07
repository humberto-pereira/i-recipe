from django.db import models
from django.contrib.auth.models import User
from recipe_posts.models import RecipePosts

class RecipeRating(models.Model):
    recipe = models.ForeignKey(RecipePosts, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-rating']
        unique_together = ('recipe', 'user')

    def __str__(self):
        return f"{self.user}'s rating of {self.recipe}: {self.rating}"
        