from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import generics, viewsets, permissions

# Create your views here.

class CustomUserRegister(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class CustomFollowerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomUserSerializer(many=True, read_only=True)
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

