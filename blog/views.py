#Import from the core django
from turtle import title
from django.shortcuts import render
from django.http import HttpResponseRedirect,FileResponse 
from django.views.generic import DeleteView,CreateView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus.paragraph import Paragraph
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

def photo_list(request):
	if request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES) # Gets the uploaded data and maps it to the ProfileForm object
		if form.is_valid(): # Checks if the uploaded data is valid or not
			form.save() # Saves the uploaded data into our Database model
			return redirect('home') # Makes the page redirect back to home
    
	else:
		form = PhotoForm()
    
	posts = Photo.objects.all()# Fetched all the data from database model
	return render(request, 'crop.html', {'form' : form, 'posts':posts}) # Return the crop.html page having form and userData passed as a dictionary    


def download_pdf(request):
    # if this is a POST request we need to process the form data
    # if 'pdf' in request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form =PostForm(request.POST)
        print("test 1")

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            buf =io.BytesIO()
            c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
            textob=c.beginText()
            textob.setTextOrigin(inch,inch)
            textob.setFont("Helvetica",14)
            lines=[]
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']            
            category = form.cleaned_data['category']
            body = form.cleaned_data['body']
            image = form.cleaned_data['image']
            publish = form.cleaned_data['publish']

            fileName = "BLOG_{0}_{1}.pdf".format(title,author)
            lines.append(f"Blog Title: {title} ")
            lines.append(f"Author: {author}")
            lines.append(f"Category: {category}")
            lines.append(f"Content:{body}") 
            # lines.append(f"Image: {image}")
            lines.append(f"Published: {publish}")
 
            for line in lines:
                textob.textLine(line )
                textob.textLine("")

            c.drawText(textob)
            c.showPage()
            c.save()
            buf.seek(0)    
            return FileResponse(buf,as_attachment=True,filename=fileName)
        else:
            return HttpResponse("form is not a valid one")    
    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = PostForm()

    # return render(request, 'blog_new.html', {'form': form})    