from django.test import TestCase
from ..models import Book

# Test your models here.
class BookModelTest(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            cover="books/images/covers/test_cover.jpg",
            genre="SciFi",
            book_file="books/pdf/test_book.pdf"
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.cover, "books/images/covers/test_cover.jpg")
        self.assertEqual(self.book.genre, "SciFi")
        self.assertEqual(self.book.book_file, "books/pdf/test_book.pdf")

    def test_str_method(self):
        self.assertEqual(str(self.book), self.book.title)
