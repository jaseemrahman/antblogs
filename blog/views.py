from django.shortcuts import render
from .models import BlogPost,Category
from django.http import Http404, HttpResponse, HttpResponseRedirect 
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from .forms import PostForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

#to add new blogs
class BlogCreateView(LoginRequiredMixin,CreateView):
    model=BlogPost
    form_class=PostForm
    template_name='blog_new.html'
    login_url='login'

    def form_valid(self,form):  
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        # Finally write the changes into database
        self.object.save()
        # redirect , indicating data was inserted successfully
        return HttpResponseRedirect(self.get_success_url())

    # for success url
    def get_success_url(self):
        return reverse_lazy('blog.detail', kwargs={'pk': self.object.pk})


#to list by category
def CategoryView(request,cats):
    category_posts=BlogPost.objects.filter(category=cats)
    return render(request,'blog_list.html',{'cats':cats.title(),'category_posts':category_posts})
    
#for blogs detail view
class BlogDetailview(DeleteView):
    model=BlogPost
    context_object_name='blogs'
    template_name='blog_detail.html'    

#to delete blogs
class BlogDeleteView(LoginRequiredMixin,DeleteView):
    model=BlogPost
    success_url="/"
    context_object_name='blogs'
    template_name='blog_delete.html'
    login_url='login'  

#to edit blogs
class BlogUpdateView(LoginRequiredMixin,UpdateView):
    model=BlogPost
    form_class=PostForm
    context_object_name='blogs'
    template_name ='blog_edit.html'  
    login_url='login'

#for success url
    def get_success_url(self):
        return reverse_lazy('blog.detail', kwargs={'pk': self.object.pk})   
     