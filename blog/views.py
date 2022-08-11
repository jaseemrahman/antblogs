from django.shortcuts import render
from .models import Post,Category
from django.http import Http404, HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .forms import PostForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class BlogCreateView(LoginRequiredMixin,CreateView):
    model=Post
    success_url="/"
    form_class=PostForm
    template_name='blog_new.html'
    login_url='login'

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class BlogListview(ListView):
    model=Post
    context_object_name='blogs'
    template_name='blog_list.html'
    # category=request.GET.get('category')
    # if category==category:
    #     blogs=Category.objects.filter(category_name=category)

    # def queryset(self,pk):
    #     return self.request.Category.objects.filter(category_id=pk)
class BlogDetailview(DeleteView):
    model=Post
    context_object_name='blogs'
    template_name='blog_detail.html'    

class BlogDeleteView(DeleteView):
    model=Post
    success_url="/"
    context_object_name='blogs'
    template_name='blog_delete.html'     

class BlogUpdateView(UpdateView):
    model=Post
    success_url="/"
    form_class=PostForm
    template_name ='blog_edit.html'       