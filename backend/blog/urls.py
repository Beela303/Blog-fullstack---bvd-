from django.urls import path
from .views import PostsView, PostView,  CategoriesView, CategoryView, CategoryPostsView

urlpatterns = [
    path('posts/', PostsView.as_view(), name='Blog Posts'),
    path('<slug:category_slug>/<slug:post_slug>/', PostView.as_view(), name='Blog Post'),
    path('categories/', CategoriesView.as_view(), name='Categories'),
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='Category'),
    path('categories/<slug:category_slug>/posts/', CategoryPostsView.as_view(), name='Posts in Category'),
]
