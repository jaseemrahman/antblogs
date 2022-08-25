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
       
#for Photo model
class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height', )

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo       