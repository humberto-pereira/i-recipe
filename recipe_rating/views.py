from rest_framework import generics, permissions
from .models import RecipeRating
from .serializers import RecipeRatingSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import ValidationError


class RecipeRatingList(generics.ListCreateAPIView):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        recipe = serializer.validated_data['recipe']

        # Check for existing rating
        if RecipeRating.objects.filter(user=user, recipe=recipe).exists():
            raise ValidationError('You have already rated this recipe.')

        serializer.save(user=user)


class RecipeRatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeRatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = RecipeRating.objects.all()
