from rest_framework import serializers
from .models import Post, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class PostSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'slug', 'created_on', 'updated_on', 'categories']
