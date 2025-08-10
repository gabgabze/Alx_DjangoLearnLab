from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('id',)

"""import datettime do the data checks against future and return data"""

    def validate(self, data):
        """get the current date"""
        current_year = datetime.now().year
        if data["published_year"] > current_year:
            raise serializers.ValidationError('Publication year cannot be in future')
        return data
