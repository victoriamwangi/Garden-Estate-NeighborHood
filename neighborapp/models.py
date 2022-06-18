from django.db import models
from django.contrib.auth.models import User
# Create your models here.


from django.db.models.signals import post_save
from django.dispatch import receiver




# class Neighborhood(models.Model):
#     name = models.CharField(max_length= 100)
#     location = models.CharField(max_length=100)
#     occupants_count = models.IntegerField(default= 0, null=True, blank=True)
    
#     def __str__(self):
#         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile')
    username= models.CharField(max_length= 100, blank=True)
    # neighborhood = models.OneToOneField(Neighborhood, on_delete= models.CASCADE)
    email = models.EmailField(max_length=100, blank=True)
    prof_image = models.ImageField(default='default.png', upload_to = 'profiles/')
    bio = models.CharField(max_length= 30, null=True, blank=True)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    second_name = models.CharField(max_length=40, null=True, blank=True)
    
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
    # neighborhood = models.OneToOneField(Neighborhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.biz_name
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null=True)
    bio = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    pub_date= models.DateTimeField(auto_now_add=True)
    
    def save_post(self):
        return self.save()
    
    @classmethod
    def get_posts(self):
        all_posts = Post.objects.all()
        return all_posts
    @classmethod
    def search_by_user(cls, user):
        posts= cls.objects.filter(user=user)
        return posts
    
    
    def __str__(self):
        return self.post_name