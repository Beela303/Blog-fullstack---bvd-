from django.urls import path
from .views import PostListCreateView, PostDetailView,  CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path('api/postlist/', PostListCreateView.as_view(), name='PostListCreateView'),
    path('api/postdetail/<int:pk>/', PostDetailView.as_view(), name='PostDetailView'),
    path('api/categorylist/', CategoryListCreateView.as_view(), name='CategoryListCreateView'),
    path('api/categorydetail/<int:pk>/', CategoryDetailView.as_view(), name='CategoryDetailView'),
]
