from django.db import models

# Create your models here.
class Book(models.Model):
  _GENRES = [
    "SciFi",
    "Fantasy",
    "Thriller",
    "Romance",
    "Mystery",
    "Autobiography",
  ]

  title = models.CharField(max_length=150)
  author = models.CharField(max_length=70)
  cover = models.ImageField(storage="books/images/covers/")
  genre = models.CharField(max_length=50, choices=_GENRES)
  book_file = models.FileField(_("PDF File"), upload_to="books/pdf/", max_length=100)