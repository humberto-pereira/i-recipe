from django.db import models
from django.contrib.auth.models import User
from recipe_category.models import Category


class RecipePosts(models.Model):

    tag_choices = [
        ('american', 'American'),
        ('argentinian', 'Argentinian'),
        ('asian', 'Asian'),
        ('baked', 'Baked'),
        ('baking', 'Baking'),
        ('barbecue', 'Barbecue'),
        ('beef', 'Beef'),
        ('breakfast', 'Breakfast'),
        ('brazilian', 'Brazilian'),
        ('british', 'British'),
        ('casseroles', 'Casseroles'),
        ('chicken', 'Chicken'),
        ('chinese', 'Chinese'),
        ('comfort', 'Comfort'),
        ('comfort_food', 'Comfort Food'),
        ('curries', 'Curries'),
        ('dairy_free', 'Dairy Free'),
        ('dessert', 'Dessert'),
        ('dinner', 'Dinner'),
        ('dips', 'Dips'),
        ('duck', 'Duck'),
        ('exotic', 'Exotic'),
        ('fish', 'Fish'),
        ('french', 'French'),
        ('fried', 'Fried'),
        ('german', 'German'),
        ('gluten_free', 'Gluten Free'),
        ('gourmet', 'Gourmet'),
        ('greek', 'Greek'),
        ('grilled', 'Grilled'),
        ('healthy', 'Healthy'),
        ('holiday_special', 'Holiday Special'),
        ('indian', 'Indian'),
        ('italian', 'Italian'),
        ('japanese', 'Japanese'),
        ('keto', 'Keto'),
        ('kid_friendly', 'Kid Friendly'),
        ('korean', 'Korean'),
        ('lamb', 'Lamb'),
        ('lebanese', 'Lebanese'),
        ('low_carb', 'Low Carb'),
        ('lunch', 'Lunch'),
        ('mediterranean', 'Mediterranean'),
        ('mexican', 'Mexican'),
        ('moroccan', 'Moroccan'),
        ('no_bake', 'No Bake'),
        ('nut_free', 'Nut Free'),
        ('one_pot', 'One Pot'),
        ('paleo', 'Paleo'),
        ('pasta', 'Pasta'),
        ('pizza', 'Pizza'),
        ('pork', 'Pork'),
        ('prawns', 'Prawns'),
        ('protein_rich', 'Protein Rich'),
        ('quick_easy', 'Quick and Easy'),
        ('quick_meals', 'Quick Meals'),
        ('raw', 'Raw'),
        ('roasted', 'Roasted'),
        ('russian', 'Russian'),
        ('salads', 'Salads'),
        ('salmon', 'Salmon'),
        ('sandwiches', 'Sandwiches'),
        ('seafood', 'Seafood'),
        ('seasonal', 'Seasonal'),
        ('shellfish', 'Shellfish'),
        ('slow_cooker', 'Slow Cooker'),
        ('slow_cooking', 'Slow Cooking'),
        ('smoked', 'Smoked'),
        ('snack', 'Snack'),
        ('soups', 'Soups'),
        ('spanish', 'Spanish'),
        ('spicy', 'Spicy'),
        ('stews', 'Stews'),
        ('stir_fried', 'Stir Fried'),
        ('street_food', 'Street Food'),
        ('sugar_free', 'Sugar Free'),
        ('thai', 'Thai'),
        ('traditional', 'Traditional'),
        ('tuna', 'Tuna'),
        ('turkey', 'Turkey'),
        ('turkish', 'Turkish'),
        ('vegan', 'Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('vietnamese', 'Vietnamese'),
        ('whole30', 'Whole30'),
        ('wraps', 'Wraps')
    ]

    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT,
                                 default=10, null=False, blank=False,
                                 related_name='recipe_posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True
    # means that the field will be automatically set when
    # the object is first created
    updated_at = models.DateTimeField(auto_now=True)  # auto_now=True
    # means that the field will be automatically set
    # every time the object is saved
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    image = models.ImageField(upload_to='images/',
                              default='../default_post_xvhdrp', blank=True)
    tags = models.CharField(max_length=100, choices=tag_choices, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
