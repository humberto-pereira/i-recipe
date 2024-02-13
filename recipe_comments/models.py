from django.db import models
from django.contrib.auth.models import User
from recipe_posts.models import RecipePosts


class RecipeComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='recipe_comments')
    post = models.ForeignKey(RecipePosts, on_delete=models.CASCADE,
                             related_name='recipe_comments')
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username} {self.content}'
