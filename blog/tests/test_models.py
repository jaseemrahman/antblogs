from django.test import TestCase
from django.template.defaultfilters import slugify
from blog.models import BlogPost


class ModelsTestCase(TestCase):
    def test_post_has_body(self):
        """Posts are given body correctly when saving"""
        blog = BlogPost.objects.create(title="test 45")
        blog.body = "content"
        blog.save()
        self.assertEqual(blog.body, slugify(blog.title))