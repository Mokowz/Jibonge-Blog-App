from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Author, Blog, Tag
from accounts.models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email'] 

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'bio', 'user']


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
        read_only_fields = ['author']

    def create(self, validated_data):
        tags_data = self.context['request'].data.get('tags')
        blog = Blog.objects.create(**validated_data)
        if tags_data:
            tags = Tag.objects.filter(id__in=tags_data)
            blog.tags.set(tags)
        return blog

    def update(self, instance, validated_data):
        tags_data = self.context['request'].data.get('tags')
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        if tags_data:
            tags = Tag.objects.filter(id__in=tags_data)
            instance.tags.set(tags)
        return instance
    