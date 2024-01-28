from django.urls import path
from recipe_comments import views

urlpatterns = [
    path('recipe_comments/', views.RecipeCommentsList.as_view()),
    path('recipe_comments/<int:pk>/', views.RecipeCommentsDetail.as_view()),
]