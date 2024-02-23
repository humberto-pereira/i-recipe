from django.urls import path
from recipe_posts import views
from .views import tag_choices

urlpatterns = [
    path('recipe-posts/', views.RecipePostsList.as_view()),
    path('recipe-posts/<int:pk>/', views.RecipePostsDetail.as_view()),
    path('tag-choices/', tag_choices, name='tag-choices'),
]