from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets

# Create your views here.

"""class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self,request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)"""

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
