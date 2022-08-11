from datetime import datetime
from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from blog.models import Category
# Create your views here.

def home(request):
    dict_date={
        "today":datetime.today(),
        "categories":Category.objects.all()
    }
    return render(request,'home.html',dict_date)

class loginInterfaceView(LoginView):
    template_name ='login.html'   

class SignupView(CreateView):
    form_class=UserCreationForm
    template_name = 'signup.html'
    success_url = '/'
#if user is authenticated.
    def get(self, request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'     
