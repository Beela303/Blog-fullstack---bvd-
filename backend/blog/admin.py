from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin) :
    list_display = ('name', 'description', 'slug')

class PostAdmin(admin.ModelAdmin) :
    list_display = ['title', 'content', 'created_on', 'status', 'category']
    list_filter = ['status']
    search_fields = ('title', 'content')

    class Meta:
         ordering = ('-created_on')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)