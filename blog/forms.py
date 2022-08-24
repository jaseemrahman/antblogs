#Import from the core django
from django.forms import ModelForm
#Import from local app/library
from .models import BlogPost

class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model= BlogPost
        fields = '__all__'

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
        category = self.cleaned_data['category']
        body = self.cleaned_data['body'].replace("\r\n","<br/>")
        publish = self.cleaned_data['publish']
        # conditions to be met for the blog body length 
        if len(body) < 100: 
            error_message = 'Minimum 100 characters required for body'
            self.add_error('body', error_message)
    
        # return any errors if found.
        return self.cleaned_data  

#to upload images
# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ('file', )          