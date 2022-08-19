from unittest.util import _MAX_LENGTH
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

#model for category
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.CharField(max_length=250)
    parent=models.ForeignKey("self", on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.category_name

#model for blogs
class BlogPost(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    body=RichTextUploadingField(max_length=5000)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        indexes=[models.Index(fields=['title','author','category'])]
        ordering=('-publish',)

    def __str__(self):
        return self.title  