from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from i_recipe_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, filters
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__recipeposts', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'user__following__followed__profile',
    ]
    ordering_fields = [
        'posts_count', 
        'followers_count',
        'following_count',
        'user__following__created_at',
        'user__followed__created_at',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.annotate(
        posts_count=Count('user__recipeposts', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('user__recipeposts', distinct=True),
        followers_count=Count('user__followed', distinct=True),
        following_count=Count('user__following', distinct=True),
    ).order_by('-created_at')


    