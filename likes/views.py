from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly

class LikeList(generics.ListCreateAPIView):
    """
    Api view to retrieve the list of all likes or create a new like
    Requires authentication
    Only authenticated users can create a new like
    Unauthenticated users can view likes
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Api view to retrieve, update or delete a like
    Requires authentication
    Only the owner of the like can update or delete it
    Unauthenticated users can view likes
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]


