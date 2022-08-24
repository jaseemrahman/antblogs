from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import BlogPost,Category


class ModelsTestCase(TestCase):
    def setUp(self):
        """Tests that require a database (namely, model tests) will not use use “real” (production) database"""
        Category.objects.create(id=1)
        User.objects.create(id=1)
    def test_post_has_body(self ):
        """Posts are given body correctly when saving"""
        cat_obj=Category.objects.get(id=1) 
        blog = BlogPost.objects.create(title="test",author_id =1 ,category=cat_obj)
        blog.body = "content"
        blog.save()
        self.assertEqual(blog.body,"content")