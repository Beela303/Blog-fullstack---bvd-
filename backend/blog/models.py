from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

class Category(models.Model) :
    name = models.CharField(max_length=30)
    description = models.TextField(null=False)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=500, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    categories = models.ManyToManyField(Category, related_name ="posts")

    class Meta :
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
class Comment(models.Model) :
    author = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
    