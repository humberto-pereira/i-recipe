from django.urls import path
from recipe_rating import views

urlpatterns = [
    path('ratings/<int:pk>/', views.RecipeRatingDetailView.as_view()),
    path('ratings/', views.RecipeRatingList.as_view()),
]
