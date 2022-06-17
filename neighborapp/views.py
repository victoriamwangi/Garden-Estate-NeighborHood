from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, PostForm
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

# @login_required(login_url='/accounts/login/')          
def new_post(request):
    user = request.user
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.user = request.user
            
            form.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/post.html', {'form': form})
           

