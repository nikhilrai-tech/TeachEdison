from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('bookstore.urls')),
    path('', include('reviews.urls')),
    path('user/', include('user.urls'))
]
