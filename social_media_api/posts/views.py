from warnings import filters

from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from accounts.serializers import CustomUserSerializer
from rest_framework import generics, viewsets, permissions



# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(author=self.request.user).order_by('-date_posted')


class PostUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        data = super(PostUserViewSet, self).get_queryset()
        if self.request.user.is_authenticated and self.request.user.follows == True:
            return self.queryset.filter(author=self.request.user).order_by('-date_posted')









class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(author=self.request.user)

