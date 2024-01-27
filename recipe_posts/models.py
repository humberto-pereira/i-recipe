from django.db import models
from django.contrib.auth.models import User

class RecipePosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the field will be automatically set when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True means that the field will be automatically set every time the object is saved
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', default='../default_post_xvhdrp', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'