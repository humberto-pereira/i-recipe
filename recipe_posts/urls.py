from django.urls import path
from recipe_posts import views
from .views import tag_choices

urlpatterns = [
    path('recipe_posts/', views.RecipePostsList.as_view()),
    path('recipe_posts/<int:pk>/', views.RecipePostsDetail.as_view()),
    path('tag-choices/', tag_choices, name='tag-choices'),
]