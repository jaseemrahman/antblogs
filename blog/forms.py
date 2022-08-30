#Import from the core django
from django.forms import ModelForm
from django import forms
from django.core.files import File
# Import from the third library
from PIL import Image
#Import from local app/library
from .models import BlogPost,Photo

class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model= BlogPost
        # fields = '__all__' 
        exclude = ['image']

        labels = {
            'title':'Blog Title',
            'body':'Share your thoughts here'
        }
        
        # this function will be used for the server side validation
    def clean(self):
        # data from the form is fetched using super function
        super(PostForm, self).clean()
        # extract the fields ield from the data

        title = self.cleaned_data['title']
        author = self.cleaned_data['author']
        category =self.cleaned_data['category']
        body =self. cleaned_data['body'].replace("\r\n","<br/>")
        # image = self.cleaned_data['image']
        print('test point')
        # publish = self.cleaned_data.get['publish']
        # conditions to be met for the blog body length 
        if len(body) < 100: 
            error_message = 'Minimum 100 characters required for body'
            self.add_error('body', error_message)
    
        # return any errors if found.
        return self.cleaned_data  
       
       
#for Photo model
class PhotoForm(forms.ModelForm):
      class Meta:
        model= Photo
        fields = ['file']    