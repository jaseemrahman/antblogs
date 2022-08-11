from django import forms
from .models import Post,Category
# from django import ModelForm

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = '__all__'