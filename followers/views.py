from rest_framework import generics, permissions
from .models import Followers
from .serializers import FollowersSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly


class FollowersList(generics.ListCreateAPIView):
    """
    Api view to retrieve the list of all followers or create a new follower
    Requires authentication
    Only authenticated users can create a new follower
    Unauthenticated users can view followers
    """
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowersDetail(generics.RetrieveDestroyAPIView):
    """
    Api view to retrieve, update or delete a follower
    Requires authentication
    Only the owner of the follower can update or delete it
    Unauthenticated users can view followers
    """
    queryset = Followers.objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [IsOwnerOrReadOnly]
