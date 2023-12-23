from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bookstore.models import *
from bookstore.serializers import *
from .serializers import ReviewSerializer

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)