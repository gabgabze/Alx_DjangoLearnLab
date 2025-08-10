from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('id',)

    def validate(self, data):
        """get the current date"""
        current_year = datetime.now().year
        if data["published_year"] > current_year:
            raise serializers.ValidationError('Publication year cannot be in future')
        return data

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'
        depth = 1