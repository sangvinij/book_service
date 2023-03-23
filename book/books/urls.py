from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from rest_framework import routers

from .views import BookViewSet, GenreViewSet, ThemeViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'book_genres', GenreViewSet)
router.register(r'book_themes', ThemeViewSet)
router.register(r'book_authors', AuthorViewSet)

urlpatterns = [
    path(r'api/v1/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
