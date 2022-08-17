from datetime import datetime
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from blog.models import Category,Post
from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
# Create your views here.

#home page view.
def home(request):
    dict_date={
        "today":datetime.today(),
        "categories":Category.objects.all(),
    } 
    return render(request,'home.html',dict_date)

def create(request):
    if request.method == 'POST':
        print("test")
        title = request.POST['title']
        author = request.POST['author']
        category = request.POST['category']
        body = request.POST['body']
        publish = request.POST['publish']
        new_post=Post(title=title,author=author,category=category,body=body,publish=publish)
        new_post.save()
        success="blog created successfully"
        print("test")
        return HttpResponse(success)    
           
    else:
        return HttpResponse("Request method is not a POST")

#login view
class loginInterfaceView(LoginView):
    template_name ='login.html'   

#signup view
class SignupView(CreateView):
    form_class=UserCreationForm
    template_name = 'signup.html'
    success_url = '/'
#if user is authenticated.
    def get(self, request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)
#logout view
class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'     
