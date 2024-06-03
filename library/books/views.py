from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin

# Create your views here.
class HomepageView(TemplateView, ContextMixin):
  template_name = "books/homepage.html"
  extra_context = {
    'active': 'home',
  }


class LibraryView(TemplateView, ContextMixin):
  template_name = "books/library.html"
  extra_context = {
    'active': 'library',
  }