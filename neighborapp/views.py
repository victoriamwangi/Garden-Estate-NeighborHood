from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'home.html') 

@login_required(login_url= '/accounts/login/')
def profile(request):
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES)
        if profileform.is_valid():
            profileform.save()
            messages.success(request, f'Your account has been updated!')
        return redirect('profile')
    
    else:
        profileform = ProfileForm()
    
  
    return render (request, 'profile/profile.html', {"profileform": profileform})
            

