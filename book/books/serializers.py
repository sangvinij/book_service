from rest_framework import serializers

from .models import Author, Book, Genre, Theme


class GetBookTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', )


class AuthorSerializer(serializers.ModelSerializer):
    book_author = GetBookTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'


class GetBookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True, read_only=True)
    genre = serializers.CharField(source='genre.genre_name')
    theme = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


class AddBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    book_genre = GetBookTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Genre
        fields = ('genre_name', 'book_genre')


class ThemeSerializer(serializers.ModelSerializer):
    book_theme = GetBookTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Theme
        fields = ('theme_name', 'book_theme')
