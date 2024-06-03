from django.urls import path, include
from .views_api import BookViewSet
from rest_framework.routers import DefaultRouter
from .views import HomepageView, LibraryView

# Create your URLs here.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = [
  path('', HomepageView.as_view(), name="homepage"),
  path('library/', LibraryView.as_view(), name="library"),
  path('api/', include(router.urls)),
]
