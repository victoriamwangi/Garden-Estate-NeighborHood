from django.contrib import admin
from .models import Profile, Business, Neighborhood, Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Post)
