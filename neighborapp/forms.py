from django import forms 
from .models import *
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("email", "prof_image","bio", "first_name", "second_name", 'neighborhood')
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =( 'username', "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude =["user_profile", "user", "hood"]
        
        
# from django_registration.forms import RegistrationForm

# from mycustomuserapp.models import MyCustomUser


# class MyCustomUserForm(RegistrationForm):
#     class Meta(RegistrationForm.Meta):
#         model = MyCustomUser