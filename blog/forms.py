from tkinter.ttk import Widget
from turtle import title
from django import forms
from .models import Post,Category
from django.forms import ModelForm
from ckeditor.fields import RichTextField 
from ckeditor.widgets import CKEditorWidget

class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model= Post
        fields = '__all__'

        labels = {
            'title':'Blog Title',
            'body':'Share your thoughts here'
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:            
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'id':str(field)
            })

        
        # this function will be used for the server side validation
    def clean(self):
            # data from the form is fetched using super function
            super(PostForm, self).clean()
            
            # extract the fields ield from the data
            title = self.cleaned_data['title']
            author = self.cleaned_data['author']
            category = self.cleaned_data['category']
            body = self.cleaned_data['body'].replace("\r\n","<br/>")
            publish = self.cleaned_data['publish']
            # conditions to be met for the username length 
            if len(body) < 100: 
                error_message = 'Minimum 100 characters required for body'
                self.add_error('body', error_message)
    
            # return any errors if found.
            return self.cleaned_data    