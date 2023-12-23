# bookstore/serializers.py
from rest_framework import serializers
from .models import Book,Author
from reviews . serializers import ReviewSerializer
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    # author = serializers.StringRelatedField()

    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Book
        exclude = ('is_active', 'is_deleted', 'is_restored')

from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']
