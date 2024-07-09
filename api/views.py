from django.shortcuts import render

# Create your views here.
# A viewset allows you to define the common behavior for actions like list, create, retrieve, update, and destroy.

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

