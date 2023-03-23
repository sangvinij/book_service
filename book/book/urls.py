from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('books.urls')),
    path(r'drf-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
