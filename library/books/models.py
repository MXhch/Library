from django.db import models

# Create your models here.
class Book(models.Model):
  _GENRES = (
    ("SciFi", "SciFi"),
    ("Fantasy", "Fantasy"),
    ("Thriller", "Thriller"),
    ("Romance", "Romance"),
    ("Mystery", "Mystery"),
    ("Autobiography", "Autobiography"),
  )

  title = models.CharField(max_length=150)
  author = models.CharField(max_length=70)
  cover = models.ImageField(storage="books/images/covers/")
  genre = models.CharField(max_length=50, choices=_GENRES)
  book_file = models.FileField("PDF File", upload_to="books/pdf/", max_length=100)

  def __str__(self):
    return self.title