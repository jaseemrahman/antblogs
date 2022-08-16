from http import client
from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from blog.models import Post

class TestViews(TestCase):

    def setUp(self):
        self.client=client()
        self.list_url=reverse('list',args=['some-slug'])
    def test_category_list_GET(self):
        response=self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog/blog_list.html')