from django.urls import path

from .views import (
  BlogList,
  BlogDetail,
  AuthorList,
  AuthorDetail,
  TagList,
  TagDetail,
)

urlpatterns = [
  path('blogs/', BlogList.as_view(), name='blog-list'),
  path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),

  path('authors/', AuthorList.as_view(), name='author-list'),
  path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),

  path('tags/', TagList.as_view(), name='tag-list'),
  path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
]