from django.urls import path
from .views import review_list

urlpatterns = [
    path('reviews/', review_list, name='review-list'),
]
