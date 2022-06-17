from django import forms 
from .models import Post, Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =["user_profile", "user"]