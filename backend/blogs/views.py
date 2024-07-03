from django.shortcuts import render
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated

from .models import Author, Blog, Tag
from .serializers import AuthorSerializer, BlogSerializer, TagSerializer

# Create your views here.
class BlogList(generics.ListCreateAPIView):
  # permission_classes = [IsAuthenticated]
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer
  filter_backends = [filters.SearchFilter, DjangoFilterBackend]
  search_fields = ['title', 'content', 'author__user__first_name', 'author__user__first_name', 'tags__name']
  filterset_fields = ['author', 'tags']

  def perform_create(self, serializer):
    user = self.request.user
    author, created = Author.objects.get_or_create(user=user)
    print(f'User: {self.request.user}')
    serializer.save(author=author)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Blog.objects.all()
  serializer_class = BlogSerializer

class AuthorList(generics.ListCreateAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer

class TagList(generics.ListCreateAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = [permissions.IsAuthenticated]
  queryset = Tag.objects.all()
  serializer_class = TagSerializer