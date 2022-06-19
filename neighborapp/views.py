from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from .models import *
from django.urls import reverse



def home(request):
    posts = Post.get_posts().order_by('-pub_date')
    businesses = Business.all_business()
    context = {
        "posts": posts,
        
        "businesses": businesses
    }
    
    return render(request, 'home.html',context ) 


@login_required(login_url= '/accounts/login/')
def profile(request, username):
    current_user = request.user
    postss = Post.get_posts()
    hoods = Neighborhood.all_hoods()    
   
    return render(request, 'profile/profile.html',{ "postss": postss, "hoods": hoods,"current_user":current_user, })

def show_profile(request, username):    
    # only view profiles in your hood 
    user = get_object_or_404(User, username=username)
    # user_posts = Post.objects.filter(user=user)
    context = {
        "user": user,
        # " user_posts":  user_posts   
    }

    
    return render(request, 'profile/user_profile.html', context)
@login_required(login_url= '/accounts/login/')
def hood(request):
    # hoody = get_object_or_404(Neighborhood, name=hood)
    neighborhoods = Neighborhood.all_hoods()
    posts = Post.get_posts().order_by('-pub_date')
    businesses = Business.all_business()
    context = {
        "neighborhoods":  neighborhoods,
        "posts": posts,
        "businesses": businesses
         
    }
    return render(request, 'hood.html', context)
 
def each_hood(request, hood_id):
    hood_posts = Post.objects.filter(hood=hood_id).order_by('-pub_date')
    businesses = Business.objects.filter(neighborhood=hood_id)
    hood = get_object_or_404(Neighborhood, id=hood_id)

    context = {
        "hood": hood,
        "hood_posts": hood_posts,
        "businesses": businesses
       
    }
    return render(request, 'hood/hood_posts.html', context)
  
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
 

       
@login_required(login_url='/accounts/login/')          
def new_post(request,):
    user = request.user
    # hood = get_object_or_404(Neighborhood, id=hood_id)
    
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post =form.save(commit=False)
            post.user = request.user
            
            form.save()
        return redirect('each_post')
    else:
        form = PostForm()
    return render(request, 'posts/post.html', {'form': form})


def show_business(request, bizname):    
    business = get_object_or_404(Business, biz_name=bizname)

    context = {
        "business": business,
       
    }
    return render(request, 'business/business.html', context)
       

def search_biz(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get('business')
        searched_business = Business.search_business(search_term)
        message = f'{search_term}'
        return render(request, 'business/search.html', {"message": message, 'businesses':searched_business})
    else:
        message = "You haven't searched for any term"
        return render(request, 'business/search.html', {'message': message})
    