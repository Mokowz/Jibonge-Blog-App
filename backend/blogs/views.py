from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Author, Blog, Tag
from .serializers import AuthorSerializer, BlogSerializer, TagSerializer

# Create your views here.
class BlogList(generics.ListCreateAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
