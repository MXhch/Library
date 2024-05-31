from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Book

# Test your api views here.
class BookAPITest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            cover="books/images/covers/test_cover.jpg",
            genre="SciFi",
            book_file="books/pdf/test_book.pdf"
        )
        self.book_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.books_url = reverse('book-list')

    def test_get_books(self):
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_get_book_detail(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_post_book(self):
        # Ensure POST request is forbidden
        data = {
            "title": "New Test Book",
            "author": "New Test Author",
            "cover": "books/images/covers/new_test_cover.jpg",
            "genre": "Fantasy",
            "book_file": "books/pdf/new_test_book.pdf"
        }
        response = self.client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_put_book(self):
        # Ensure PUT request is forbidden
        data = {
            "title": "Updated Test Book",
            "author": "Updated Test Author",
            "cover": "books/images/covers/updated_test_cover.jpg",
            "genre": "Mystery",
            "book_file": "books/pdf/updated_test_book.pdf"
        }
        response = self.client.put(self.book_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book(self):
        # Ensure DELETE request is forbidden
        response = self.client.delete(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
