from django import forms
from .models import Post, Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'tags', 'content')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pic_url', 'banner_url', 'bday', 'motto')