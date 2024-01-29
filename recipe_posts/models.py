from django.db import models
from django.contrib.auth.models import User

class RecipePosts(models.Model):
    tag_choices = [
    ('gluten_free', 'Gluten Free'),
    ('vegetarian', 'Vegetarian'),
    ('spicy', 'Spicy'),
    ('vegan', 'Vegan'),
    ('low_carb', 'Low Carb'),
    ('dairy_free', 'Dairy Free'),
    ('quick_easy', 'Quick and Easy'),
    ('healthy', 'Healthy'),
    ('nut_free', 'Nut Free'),
    ('sugar_free', 'Sugar Free'),
    ('comfort_food', 'Comfort Food'),
    ('kid_friendly', 'Kid Friendly'),
    ('seafood', 'Seafood'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('dessert', 'Dessert'),
    ('snack', 'Snack'),
    ('seasonal', 'Seasonal'),
    ('exotic', 'Exotic'),
    ('traditional', 'Traditional'),
    ('italian', 'Italian'),
    ('mexican', 'Mexican'),
    ('asian', 'Asian'),
    ('mediterranean', 'Mediterranean'),
    ('indian', 'Indian'),
    ('french', 'French'),
    ('baked', 'Baked'),
    ('grilled', 'Grilled'),
    ('slow_cooker', 'Slow Cooker'),
    ('one_pot', 'One Pot'),
    ('no_bake', 'No Bake'),
    ('holiday_special', 'Holiday Special'),
    ('protein_rich', 'Protein Rich'),
    ('keto', 'Keto'),
    ('paleo', 'Paleo'),
    ('whole30', 'Whole30')
]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the field will be automatically set when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True means that the field will be automatically set every time the object is saved
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/', default='../default_post_xvhdrp', blank=True)
    tags = models.CharField(max_length=100, choices=tag_choices, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'