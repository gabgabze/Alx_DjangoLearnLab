from django.shortcuts import render
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics, viewsets, permissions, status


# Create your views here.

class CustomUserRegister(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CustomFollowerViewSet(generics.GenericAPIView):
    serializer_class = CustomUserSerializer(many=True, read_only=True)
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    # create a custom method overrider to handle the following loging
    def perform_create(self, serializer):
        follower = self.request.user.followers.all()
        if follower:
            serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
