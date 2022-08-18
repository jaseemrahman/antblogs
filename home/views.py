from datetime import datetime
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from blog.models import Category,BlogPost
from django.shortcuts import render
from blog.models import BlogPost
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
    try:
        if request.method == 'POST':
            title = request.POST['title']
            author = request.user
            category_id = request.POST['category']
            body = request.POST['body']
            publish = request.POST['publish']
            cat_obj=Category.objects.get(pk=category_id) 
            new_blog=BlogPost(title=title,author=author,category=cat_obj,body=body,publish=publish)
            new_blog.save()
            success="Blog Created Successfully"
            return HttpResponse(success)        
    except:
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
