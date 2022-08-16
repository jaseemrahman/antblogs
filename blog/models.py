from unicodedata import category
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

#model for category
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.CharField(max_length=250)

    def __str__(self):
        return self.category_name

#model for blogs
class Post(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    body=RichTextField(max_length=5000)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        indexes=[models.Index(fields=['title','author','category'])]
        ordering=('-publish',)

    def __str__(self):
        return self.title  