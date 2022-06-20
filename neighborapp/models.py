from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db.models.signals import post_save
from django.dispatch import receiver




class Neighborhood(models.Model):
    name = models.CharField(max_length= 100)
    location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default= 0, null=True, blank=True)
    health_contact= models.CharField(max_length= 20, blank=True)
    police_contact = models.CharField(max_length=30, blank=True)
    hood_profile = models.ImageField(default='default.png', upload_to = 'hoods/')
    
    @classmethod
    def all_hoods(self):
        hoods =Neighborhood.objects.all()
        return hoods
    
    def save_hood(self):
        return self.save()
    def delete_hood(self):
        return self.delete()
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile')
    username= models.CharField(max_length= 100, blank=True)
    neighborhood = models.OneToOneField(Neighborhood, on_delete= models.CASCADE, null= True)
    email = models.EmailField(max_length=100, blank=True)
    prof_image = models.ImageField(default='default.png', upload_to = 'profiles/')
    bio = models.CharField(max_length= 30, null=True, blank=True)
    first_name = models.CharField(max_length=40, null=True)
    second_name = models.CharField(max_length=40, null=True)
    
    @receiver(post_save, sender=User,) 
    def create_profile(sender, instance, created, **kwargs, ):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()
  
    
    def __str__(self):
        return f'{self.user.username} Profile'
class Business(models.Model):
    biz_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    neighborhood = models.ManyToManyField(Neighborhood, related_name= 'business',null= True )    
    description = models.CharField(max_length=200,  null=True)
    business_url =  models.CharField(max_length=200,  null=True)
    business_email = models.CharField(max_length=100, null=True)
    business_image = models.ImageField(default='default.png', upload_to = 'business/')
    
    @classmethod
    def all_business(self):
        businesses = Business.objects.all()
        return businesses
    @classmethod
    def search_business(cls, search_term):
        business = cls.objects.filter(biz_name__icontains = search_term)
        return business   
    def __str__(self):
        return self.biz_name
    
class Post(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name="posts")
    description = models.CharField(max_length=255)
    hood = models.ForeignKey(Neighborhood, on_delete = models.CASCADE, null=True)
    image = models.ImageField(upload_to='posts/')
    pub_date= models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        return self.save()
    def delete_post(self):
        return self.delete()
    @classmethod
    def get_posts(self):
        all_posts = Post.objects.all()
        return all_posts
    @classmethod
    def get_post_by_hood(cls, hood, ):
        posts= cls.objects.filter(hood = hood)
        return posts
    
    
    @classmethod
    def search_by_user(cls, user):
        posts= cls.objects.filter(user=user)
        return posts
    
    
    def __str__(self):
        return self.description