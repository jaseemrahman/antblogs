from django.test import TestCase
from blog.models import BlogPost,Category
from django.contrib.auth.models import User


class ModelsTestCase(TestCase):
    def test_post_has_body(self ):
        """Posts are given body correctly when saving"""
        author_id =User.id
        # author_id.save()
        category_id = '2'
        cat_obj=Category.objects.get(pk=category_id) 
        # cat_obj.save()
        blog = BlogPost.objects.create(title="test",author_id = author_id,category=cat_obj)
        blog.body = "content"
        blog.save()
        self.assertEqual(blog.body,"content")