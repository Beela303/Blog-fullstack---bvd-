from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin) :
    list_display = ('title', 'content', 'status', 'created_on', 'updated_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepoluted_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
