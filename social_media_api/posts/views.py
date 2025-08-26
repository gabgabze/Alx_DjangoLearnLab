from django.shortcuts import render, get_object_or_404
from accounts.models import CustomUser
from notifications.models import Notification
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer,LikeSerializer
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

class PostUserViewSet(generics.ListAPIView):
    queryset = Post.objects.filter(author__in=following.all()).order_by('created_at')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    following_users = CustomUser.objects.filter(id__in = follows)

    """def get_queryset(self):
        data = super(PostUserViewSet, self).get_queryset()
        if self.request.user.is_authenticated and self.request.user.follows == True:
            return Post.objects.filter(author__in=following_users).order_by", "following.all()"
            #return self.queryset.filter(author=self.request.user).order_by('-date_posted')"""

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(author=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.get_or_create(user=request.user, post=post)
    posts = generics.get_object_or_404(Post, pk=pk)
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    notifications = Notification.objects.create()

