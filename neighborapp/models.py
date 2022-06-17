from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length= 100)
    location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default= 0, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, related_name= 'profile')
    username= models.CharField(max_length= 100, blank=True)
    neighborhood = models.OneToOneField(Neighborhood, on_delete= models.CASCADE)
    email = models.EmailField(max_length=100)
    
    def save_profile(self):
        return self.save()
    
    def __str__(self):
        return f'{self.user.username}-{self.created}'
class Business(models.Model):
    biz_name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    neighborhood = models.OneToOneField(Neighborhood, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.biz_name
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    user_profile = models.ForeignKey(Profile, on_delete = models.CASCADE, null=True)
    bio = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    
    def save_post(self):
        return self.save()
    
    
    def __str__(self):
        return self.post_name