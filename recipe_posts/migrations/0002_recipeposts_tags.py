# Generated by Django 3.2.22 on 2024-01-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeposts',
            name='tags',
            field=models.CharField(blank=True, choices=[('gluten_free', 'Gluten Free'), ('vegetarian', 'Vegetarian'), ('spicy', 'Spicy'), ('vegan', 'Vegan'), ('low_carb', 'Low Carb'), ('dairy_free', 'Dairy Free'), ('quick_easy', 'Quick and Easy'), ('healthy', 'Healthy'), ('nut_free', 'Nut Free'), ('sugar_free', 'Sugar Free'), ('comfort_food', 'Comfort Food'), ('kid_friendly', 'Kid Friendly'), ('seafood', 'Seafood'), ('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('snack', 'Snack'), ('seasonal', 'Seasonal'), ('exotic', 'Exotic'), ('traditional', 'Traditional'), ('italian', 'Italian'), ('mexican', 'Mexican'), ('asian', 'Asian'), ('mediterranean', 'Mediterranean'), ('indian', 'Indian'), ('french', 'French'), ('baked', 'Baked'), ('grilled', 'Grilled'), ('slow_cooker', 'Slow Cooker'), ('one_pot', 'One Pot'), ('no_bake', 'No Bake'), ('holiday_special', 'Holiday Special'), ('protein_rich', 'Protein Rich'), ('keto', 'Keto'), ('paleo', 'Paleo'), ('whole30', 'Whole30')], max_length=100),
        ),
    ]
