from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Author, Book, Genre, Theme


class BookTests(APITestCase):
    def setUp(self):
        self.genre = Genre.objects.create(genre_name='Scientific literature')
        self.theme = Theme.objects.create(theme_name='History')
        self.author = Author.objects.create(
            first_name='Graham',
            last_name='McNeill'
        )
        self.book = Book.objects.create(
            title='Winged Hussars',
            genre=self.genre,
        )
        self.book.author.add(self.author)
        self.book.theme.add(self.theme)

    def test_get_requests(self):
        list_of_urls = ['book-list', 'genre-list', 'author-list', 'theme-list']
        list_of_response_status_codes = []
        for url in list_of_urls:
            response = self.client.get(reverse(url))
            list_of_response_status_codes.append(response.status_code)
        self.assertTrue(all(status_code == 200
                            for status_code in list_of_response_status_codes))

    def test_create_author(self):
        url = reverse('author-list')
        response = self.client.post(url, data={
            'first_name': 'Dan',
            'last_name': 'Abnett'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book(self):
        url = reverse('book-list')
        response = self.client.post(url, data={
            'title': 'Horus heresy',
            'author': [self.author.pk],
            'genre': self.genre.pk,
            'theme': [self.theme.pk]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_author(self):
        url = reverse('author-detail', kwargs={'pk': self.author.pk})
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.json().get('first_name'), 'Graham')
        response_patch = self.client.patch(url, data={'first_name': 'Marilyn'})

        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(response_patch.json().get('first_name'), 'Marilyn')

        response_delete = self.client.delete(url)
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response_get = self.client.get(url)

        self.assertEqual(response_get.status_code, status.HTTP_200_OK)
        self.assertEqual(response_get.json().get('title'), 'Winged Hussars')

        response_patch = self.client.patch(url, data={'title': 'Roman Empire'})
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(response_patch.json().get('title'), 'Roman Empire')

        response_delete = self.client.delete(url)
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
