from django.test import TestCase
from django.template.defaultfilters import slugify
from blog.models import BlogPost


class ModelsTestCase(TestCase):
    def test_post_has_slug(self):
        """Posts are given slugs correctly when saving"""
        blog = BlogPost.objects.create(title="My first post")

        blog.author = "John Doe"
        blog.save()
        self.assertEqual(blog.slug, slugify(blog.title))

