from django.db.models import Avg
from rest_framework import generics, permissions
from i_recipe_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .models import RecipeRating, RecipePosts
from .serializers import RecipeRatingSerializer



class RecipeRatingList(generics.ListCreateAPIView):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeRatingDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = RecipeRatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = RecipeRating.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj
