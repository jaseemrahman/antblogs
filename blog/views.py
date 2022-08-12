from django.shortcuts import render
from .models import Post,Category
from django.http import Http404, HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .forms import PostForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#to add new blogs
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

#to list by category
def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request,'blog_list.html',{'cats':cats.title(),'category_posts':category_posts})
    
#for blogs detail view
class BlogDetailview(DeleteView):
    model=Post
    context_object_name='blogs'
    template_name='blog_detail.html'    

#to delete blogs
class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url="/"
    context_object_name='blogs'
    template_name='blog_delete.html'
    login_url='login'     

#to edit blogs
class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=Post
    success_url="/"
    form_class=PostForm
    context_object_name='blogs'
    template_name ='blog_edit.html'  
    login_url='login'   
     