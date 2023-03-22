from django.core.validators import RegexValidator
from django.db import models


class Book(models.Model):
    year_regex = RegexValidator(regex=r'^\d{1,4}$')
    title = models.CharField(max_length=255)
    author = models.ManyToManyField('author')
    cover = models.ImageField(upload_to='images/books', null=True, blank=True)
    genre = models.ForeignKey('genre', on_delete=models.CASCADE)
    theme = models.ManyToManyField('theme')
    year_published = models.CharField(max_length=4, validators=[year_regex])
    description = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/authors', null=True, blank=True)
    short_biography = models.TextField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_author')
        ]


class Genre(models.Model):
    genre_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.genre_name}'


class Theme(models.Model):
    theme_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.theme_name}'

