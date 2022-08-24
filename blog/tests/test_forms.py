from django.test import TestCase
from django.contrib.auth.models import User

from blog.forms import PostForm
from blog.models import Category

class MyTests(TestCase):
    def setUp(self):
        """Tests that require a database (namely, model tests) will not use use “real” (production) database"""
        Category.objects.create(id=1)
        User.objects.create(id=1)
    def test_forms(self):
        cat_obj=Category.objects.get(id=1) 
        form_data = {'title': 'something',
                    'author':1,
                    'category':cat_obj,
                    'body':"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
                    'publish':'2022-08-18 05:11:00'}
        form = PostForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())