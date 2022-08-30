from django.urls import path,include
from .import views

urlpatterns = [
    path('blog/category/<str:cats>/',views.CategoryView,name='blog.list'),
    path('blog/<int:pk>', views.BlogDetailview.as_view(),name='blog.detail'),
    path('blog/new', views.BlogCreateView.as_view(),name='blog.new'),
    path('blog/<int:pk>/edit', views.BlogUpdateView.as_view(),name='blog.edit'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(),name='blog.delete'),
    path('blog/upload', views.upload,name='uploads'),
    path('blog/upload/file', views.file_upload),
    path('blog/upload/photo', views.photo_list,name="photo.list"),
    # path('blog/upload/photo/pdf', views.download_pdf,name="pdf"),
]