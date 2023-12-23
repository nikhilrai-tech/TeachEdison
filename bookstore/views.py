from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from reviews . models import *
from reviews . serializers import ReviewSerializer
from django.core.exceptions import ValidationError
from django.views.decorators.cache import cache_page
from django.db import transaction
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET'])
@cache_page(60 * 1)
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def get_books(request):
    try:
        author = request.query_params.get('author', None)
        genre = request.query_params.get('genre', None)
        publication_year = request.query_params.get('publication_year', None)
        queryset = Book.objects.filter(is_active=True, is_deleted=False)
        if author:
            queryset = queryset.filter(author__name=author)
        if genre:
            queryset = queryset.filter(genre=genre)
        if publication_year:
            queryset = queryset.filter(publication_year=publication_year)

        if not any([author, genre, publication_year]):
            queryset = Book.objects.filter(is_active=True, is_deleted=False)

        paginator = CustomPageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = BookSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    except ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def get_book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk, is_active=True, is_deleted=False)
        book_serializer = BookSerializer(book)
        reviews = book.review_set.all()
        reviews_serializer = ReviewSerializer(reviews, many=True)
        book_data = book_serializer.data
        book_data['reviews'] = reviews_serializer.data
        return Response(book_data)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def create_book(request):
    try:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Book Created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@transaction.atomic
@api_view(['PUT', 'PATCH'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        serializer = BookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Book Updated'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def soft_delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk, is_deleted=False)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
        book.is_deleted = True
        book.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def restore_book(request, pk):
    try:
        book = Book.objects.get(pk=pk, is_deleted=True)
        book.is_deleted = False
        book.is_restored = True
        book.save()
        return Response({'success': 'Book restored'},status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def create_author(request):
    try:
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Author created'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)