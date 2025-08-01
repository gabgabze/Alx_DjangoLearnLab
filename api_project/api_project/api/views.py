from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer

# Create your views here.
"""Let us create the serializers view"""
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #permission_classes = (IsAuthenticated,)

