from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

# Create your views here.

class BookList(ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    """def list(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)"""
