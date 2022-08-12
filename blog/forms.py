from tkinter.ttk import Widget
from django import forms
from .models import Post,Category
from django.forms import ModelForm
# from formValidationApp.models import *
# from django import ModelForm

class PostForm(ModelForm):
    class Meta:
        model= Post
        fields = '__all__'

        labels = {
            'title':'Blog Title',
            'body':'Share your thoughts here'
        }
        
        # this function will be used for the validation
    def clean(self):
    
            # data from the form is fetched using super function
            super(PostForm, self).clean()
            
            # extract the fields ield from the data
            title = self.cleaned_data['title']
            author = self.cleaned_data['author']
            category = self.cleaned_data['category']
            body = self.cleaned_data['body'].replace("\r\n","<br/>")
            publish = self.cleaned_data['publish']
    
            # return any errors if found
            return self.cleaned_data    