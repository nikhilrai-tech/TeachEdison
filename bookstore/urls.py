from django.urls import path
from .views import (
    get_books,
    get_book_detail,
    create_book,
    update_book,
    soft_delete_book,
    restore_book,create_author
)

urlpatterns = [
    path('books/', get_books, name='get-books'),
    path('books/<int:pk>/', get_book_detail, name='get-book-detail'),
    path('books/<int:pk>/update/', update_book, name='update-book'),
    path('books/<int:pk>/delete/', soft_delete_book, name='soft-delete-book'),
    path('books/<int:pk>/restore/', restore_book, name='restore-book'),
    path('books/create/', create_book, name='create-book'),
    path('author/', create_author, name='create_author'),
]
