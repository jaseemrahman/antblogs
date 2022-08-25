#Import from the core django
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Import from the third library
from ckeditor.fields import RichTextField
from PIL import Image


# Create your models here.
#model for category
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    category_description=models.CharField(max_length=250)
    parent=models.ForeignKey("self", on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.category_name

#model for images        
class Photo(models.Model):
    file=models.ImageField(upload_to='photos/')
    date = models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering=['-date']

    def __str__(self):
        return str(self.file)

#model for blogs
class BlogPost(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    body=RichTextField(max_length=4000)
    image=models.ManyToManyField(Photo,blank=True)
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        #indexing.
        indexes=[models.Index(fields=['title','author','category'])]
        ordering=('-publish',)

    def __str__(self):
        return self.title     