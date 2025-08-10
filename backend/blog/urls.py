from django.urls import path
from rest_framework import routers
from . import views
from .views import ( PostsView, PostView, PostDetailView,  CategoriesView, CategoryView, CategoryPostsView, CommentListView, CommentDetailView, RecentPostsView)

urlpatterns = [
    path('posts/', PostsView.as_view(), name='Blog Posts'),
    path('posts/<int:id>', PostDetailView.as_view(), name='Blog Post Detail'),
    path('<slug:category_slug>/<slug:post_slug>/', PostView.as_view(), name='Blog Post'),

    path('categories/', CategoriesView.as_view(), name='Categories'),
    path('categories/<slug:category_slug>/', CategoryView.as_view(), name='Category'),
    path('categories/<slug:category_slug>/posts/', CategoryPostsView.as_view(), name='Posts in Category'),

    path('comments/<slug:post_slug>', CommentListView.as_view(), name='Comments'),
    path('comments/<slug:post_slug>/detail', CommentDetailView.as_view(), name='Comment Detail'),
]

router = routers.DefaultRouter()
router.register(r'posts/recentposts', RecentPostsView, basename="Recent Posts")

urlpatterns += router.urls