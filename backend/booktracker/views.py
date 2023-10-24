from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Create your views here.
class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorView(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

