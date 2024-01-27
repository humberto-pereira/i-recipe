from django.urls import path
from recipe_posts import views

urlpatterns = [
    path('recipe_posts/', views.RecipePostsList.as_view()),
]