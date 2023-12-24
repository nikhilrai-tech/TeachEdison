from rest_framework import serializers
from .models import Review
from bookstore. models import *
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment', 'created_at', 'book', 'user']

    def validate(self, data):
        book = data['book']
        if book.is_deleted:
            raise serializers.ValidationError("Book Deleted")

        return data