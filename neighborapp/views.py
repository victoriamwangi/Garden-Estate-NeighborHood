from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.urls import reverse



def home(request):
    posts = Post.get_posts().order_by('-pub_date')
    hoods = Neighborhood.all_hoods()
    businesses = Business.all_business()
    context = {
        "posts": posts,
        "hoods": hoods,
        "businesses": businesses
    }
    
    return render(request, 'home.html',context ) 

@login_required(login_url= '/accounts/login/')
def profile(request, username):
    current_user = request.user
    user = current_user
    posts = Post.search_by_user(user)
    return render(request, 'profile/profile.html',)
  
  
@login_required(login_url= '/accounts/login/')
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        profileform = ProfileForm(request.POST, request.FILES, instance= request.user.profile)    
        if profileform.is_valid():           
            profileform.save()
        return redirect( 'profile', user.username)
    else:
        profileform = ProfileForm(instance = request.user.profile)
        
    context ={
            "profileform": profileform
    }
    return render(request, "profile/update_profile.html", context)
 
def show_profile(request, username):    
    user = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(user=user)
    context = {
        "user": user,
        " user_posts":  user_posts   
    }
    return render(request, 'profile/user_profile.html', context)
       
@login_required(login_url='/accounts/login/')          
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


def show_business(request, bizname):    
    business = get_object_or_404(Business, biz_name=bizname)

    context = {
        "business": business,
       
    }
    return render(request, 'business/business.html', context)
       
