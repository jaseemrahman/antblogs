from django.urls import reverse,resolve
from django.test import SimpleTestCase

from blog.views import BlogCreateView,CategoryView,BlogDetailview,BlogDeleteView,BlogUpdateView


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url=reverse('blog.list',args=['some-slug'])
        self.assertEquals(resolve(url).func,CategoryView)

    def test_create_url_resolves(self):
        url=reverse('blog.new')
        self.assertEquals(resolve(url).func.view_class,BlogCreateView)

    def test_detail_url_resolves(self):
        url=reverse('blog.detail',args=['1'])
        self.assertEquals(resolve(url).func.view_class,BlogDetailview)        

    def test_update_url_resolves(self):
        url=reverse('blog.edit',args=['1'])
        self.assertEquals(resolve(url).func.view_class,BlogUpdateView)        

    def test_delete_url_resolves(self):
        url=reverse('blog.delete',args=['1'])
        self.client.delete(url)
        self.assertEquals(resolve(url).func.view_class,BlogDeleteView)                