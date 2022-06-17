from django import forms 
from .models import *
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username","email", "prof_image","bio", "first_name", "second_name")
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =( 'username', "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =["user_profile", "user"]