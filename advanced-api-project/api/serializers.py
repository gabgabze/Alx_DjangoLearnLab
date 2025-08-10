from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author',)
        read_only_fields = ('id',)
        exclude = ('publication_year',)
