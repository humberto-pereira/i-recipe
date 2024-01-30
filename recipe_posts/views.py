from django.db.models import Count
from rest_framework import permissions, generics, filters
from .models import RecipePosts
from .serializers import RecipePostsSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly

class RecipePostsList(generics.ListCreateAPIView):
    serializer_class  = RecipePostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = RecipePosts.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('recipe_comments', distinct=True),
    ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter]
    ordering_fields = [
        'likes_count', 
        'comments_count',
        'likes__created_at'
    ]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipePostsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipePostsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = RecipePosts.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('recipe_comments', distinct=True),
    ).order_by('-created_at')