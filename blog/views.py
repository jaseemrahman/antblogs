#Import from the core django
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.views.generic import DeleteView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
#Import from local app/library
from .models import BlogPost,Photo
from .forms import PostForm,PhotoForm


# Create your views here.

#to add new blogs
class BlogCreateView(LoginRequiredMixin,CreateView):
    model=BlogPost
    form_class=PostForm
    template_name='blog_new.html'
    login_url='login'
#code to check the form is valid.
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

# view function to upload mutiple images
def upload(request):
    images=Photo.objects.all()
    context={
        'images':images
    }
    return render(request, 'upload_image.html', context)
def file_upload(request):  
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        Photo.objects.create(file=my_file)
        return HttpResponse('Images Uploaded Successfully')
    return JsonResponse({'post':'false'})

#view function to upload and crop images
def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})    