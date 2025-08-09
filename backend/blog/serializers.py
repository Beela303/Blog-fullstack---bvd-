from rest_framework import serializers
from .models import Post, Category, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'get_absolute_url']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    category = CategorySerializer(read_only=True)
    ##category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'slug', 'created_on', 'updated_on', 'category', 'get_absolute_url']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'email', 'body', 'created_on']