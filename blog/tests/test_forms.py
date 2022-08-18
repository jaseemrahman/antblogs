from django.test import TestCase
from blog.forms import PostForm

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'title': 'something',
                    'author':'admin',
                    'category':'sports',
                    'body':'content',
                    'publish':'2022-08-18 05:11:00'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())