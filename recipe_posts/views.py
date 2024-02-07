from django.db.models import Count
from i_recipe_api.permissions import IsOwnerOrReadOnly
from django.db.models import Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import RecipePosts
from .serializers import RecipePostsSerializer, RecipePostWithRatingSerializer

class RecipePostsList(generics.ListCreateAPIView):
    serializer_class = RecipePostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['user__followed__user__profile', 'likes__user__profile', 'user__profile']
    search_fields = ['title', 'content', 'user__username', 'tags']
    ordering_fields = ['likes_count', 'comments_count', 'likes__created_at', 'average_rating']

    def get_queryset(self):
        """
        Annotate the queryset with an 'average_rating' field and allow ordering by it.
        """
        queryset = RecipePosts.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('recipe_comments', distinct=True),
            average_rating=Avg('ratings__rating')
        ).order_by('-created_at')
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipePostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipePostWithRatingSerializer 
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return RecipePosts.objects.annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('recipe_comments', distinct=True),
            average_rating=Avg('ratings__rating')
        )
