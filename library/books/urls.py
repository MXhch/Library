from django.urls import path, include
from .views_api import BookViewSet
from rest_framework.routers import DefaultRouter

# Create your URLs here.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
urlpatterns = [
  path('api/', include(router.urls))
]
