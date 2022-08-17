from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('create', views.create,name='create'),
    path('login', views.loginInterfaceView.as_view(),name='login'),
    path('signup', views.SignupView.as_view(),name='signup'),
    path('logout', views.LogoutInterfaceView.as_view(),name='logout'),
]