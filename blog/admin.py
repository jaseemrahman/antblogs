from django.contrib import admin
from .models import BlogPost,Category,Photo

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Photo)