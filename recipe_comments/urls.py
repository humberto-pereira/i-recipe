from django.urls import path
from recipe_comments import views

urlpatterns = [
    path('comments/<int:pk>/', views.RecipeCommentsDetail.as_view()),
    path('comments/', views.RecipeCommentsList.as_view()),
]
