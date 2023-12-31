from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class TestAPI(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
