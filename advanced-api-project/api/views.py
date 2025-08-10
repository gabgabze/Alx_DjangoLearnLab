from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import BookSerializer,AuthorSerializer
# Create your views here.

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.all()

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def get_object(self):
        return Book.objects.get(pk=self.kwargs['pk'])

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_update(self, serializer):
        return serializer.save(author=self.request.user)

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_destroy(self, serializer):
        return serializer.delete(author=self.request.user)

