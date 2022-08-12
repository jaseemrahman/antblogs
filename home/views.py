from datetime import datetime
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from blog.models import Category,Post
# Create your views here.

#home page view.
def home(request):
    dict_date={
        "today":datetime.today(),
        "categories":Category.objects.all(),
    } 
    return render(request,'home.html',dict_date)

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
