from rest_framework import serializers

from .models import Author, Blog, Tag
from accounts.models import CustomUser


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    tags=TagSerializer(many=True, read_only=True)
    author=AuthorSerializer(read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'tags', 'created_at']
        # read_only_fields = ['author']
    