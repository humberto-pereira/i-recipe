from django.db.models import Count
from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__followed__user__profile',
        'likes__user__profile',
        'user__profile',
    ]
    search_fields = [
        'title',
        'content',
        'user__username',
        'tags'
    ]
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