from django import forms
from .models import Post, Profile

class PostForm(forms.ModelForm):
    tweet = forms.URLField()
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('tweet', 'content')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pic_url', 'banner_url', 'bday', 'motto')