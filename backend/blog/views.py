from django.shortcuts import render, Http404

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

# Blog Views
class PostsView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def get_object(self, category_slug, post_slug):
        try:
            return Post.objects.filter(category__slug = category_slug).get(slug = post_slug)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, post_slug, format = None):
        post = self.get_object(category_slug, post_slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)

# Category Views
class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug = category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format = None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
class CategoryPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(category__slug = self.kwargs['slug'])