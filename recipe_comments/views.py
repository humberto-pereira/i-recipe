from rest_framework import generics, permissions
from .models import RecipeComments
from .serializers import RecipeCommentsSerializer, RecipeCommentsDetailSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class RecipeCommentsList(generics.ListCreateAPIView):
    """
    Api view to retrieve the list of all comments or create a new comment
    Requires authentication
    Only authenticated users can create a new comment
    Unauthenticated users can view comments
    """
    queryset = RecipeComments.objects.all()
    serializer_class = RecipeCommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post'
    ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeCommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Api view to retrieve, update or delete a comment
    Requires authentication
    Only the owner of the comment can update or delete it
    Unauthenticated users can view comments
    """
    queryset = RecipeComments.objects.all()
    serializer_class = RecipeCommentsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
