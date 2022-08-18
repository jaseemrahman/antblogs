from urllib import response
from django.test import TestCase,Client
from django.urls import reverse
from blog.models import BlogPost
from http import client

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('blog.list',args=['1'])
    def test_category_list_GET(self):
        response=self.client.get(self.list_url)

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog_list.html')
       