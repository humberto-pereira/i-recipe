from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RecipePosts
from .serializers import RecipePostsSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly

class RecipePostsList(APIView):
    serializer_class = RecipePostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        recipe_posts = RecipePosts.objects.all()
        serializer = RecipePostsSerializer(recipe_posts, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RecipePostsSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RecipePostsDetail(APIView):
    serializer_class = RecipePostsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            recipe_posts = RecipePosts.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipe_posts)
            return recipe_posts
        except RecipePosts.DoesNotExist:
            raise Http404
        
    def get (self, request, pk):
        recipe_posts = self.get_object(pk)
        serializer = RecipePostsSerializer(recipe_posts, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        recipe_posts = self.get_object(pk)
        serializer = RecipePostsSerializer(recipe_posts, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        recipe_posts = self.get_object(pk)
        recipe_posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)