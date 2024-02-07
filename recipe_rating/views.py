from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import RecipeRating
from .serializers import RecipeRatingSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly


class RecipeRatingList(generics.ListCreateAPIView):
    queryset = RecipeRating.objects.all()
    serializer_class = RecipeRatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Extract recipe ID and rating value from the request
        recipe_id = self.request.data.get('recipe')
        rating_value = self.request.data.get('rating')

        # Ensure the rating value is converted to an integer
        rating_value = int(rating_value) if rating_value is not None else None

        # Perform the update or create operation
        rating, created = RecipeRating.objects.update_or_create(
            user=self.request.user, 
            recipe_id=recipe_id,
            defaults={'rating': rating_value}
        )

class RecipeRatingDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = RecipeRatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = RecipeRating.objects.all()

    def get_object(self):
        obj = super().get_object()
        return obj
