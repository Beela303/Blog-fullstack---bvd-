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
    slug = models.SlugField(max_length=500, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/categories/{self.slug}/'

class Post(models.Model) :
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(max_length=500, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category, related_name ="posts", on_delete=models.CASCADE)

    class Meta :
        ordering = ['-created_on']

    def __str__(self):
        return self.title
        return self.author

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
class Comment(models.Model) :
    author = models.CharField(max_length=60)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
    