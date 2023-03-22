from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Author, Book, Genre, Theme


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('show_cower', 'title', 'genre', 'description')
    list_filter = ('title', 'genre')
    search_fields = ('title', 'genre')
    ordering = ('title', 'genre')

    def show_cower(self, obj):
        if obj.cover:
            return mark_safe(f"<img src ={obj.cover.url} width='60' />")
        return None

    show_cower.__name__ = 'cover'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('show_photo', 'first_name', 'last_name', 'short_biography')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', )

    def show_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src ={obj.photo.url} width='60' />")
        return None

    show_photo.__name__ = 'photo'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('genre_name', )


@admin.register(Theme)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('theme_name', )
