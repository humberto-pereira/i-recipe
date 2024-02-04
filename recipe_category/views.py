from rest_framework import generics, permissions
from .models import Category
from .serializers import CategorySerializer

# List all categories or create a new one (admin only for creation)
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Allow any user to view categories, but only admin can create new ones
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        # If the request is a safe operation (GET, HEAD, OPTIONS), allow it
        if self.request.method in permissions.SAFE_METHODS:
            return [permissions.AllowAny()]
        # For create operation (POST), require admin permissions
        return [permissions.IsAdminUser()]

# Retrieve, update, or delete a category (admin only for update/delete)
class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Only admin users can update or delete categories
    permission_classes = [permissions.IsAdminUser]
