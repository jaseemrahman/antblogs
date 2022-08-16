from django.test import TestCase
from blog.forms import PostForm

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'something': 'something'}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())