from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

# Create here your api views.
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
