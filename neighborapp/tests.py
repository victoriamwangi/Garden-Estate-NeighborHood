from django.test import TestCase
from .models import *

# Create your tests here.
# class ProfileTestCase(TestCase):
#     def setUp(self):
#         self.user = User(username='vicky')
#         self.user.save()
#         self.vicprof = Profile(user = self.user, prof_image = "jpg", bio = "lets see", first_name = "vic", second_name= 'banks', )
#         self.vicprof.save_profile()  
#     def test_instance(self):
#         self.assertTrue(isinstance(self.vicprof, Profile ))

#     def test_save_method(self):
#         self.vicprof.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)
#     def test_delete_method(self):
#         self.vicprof.delete_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) == 0)
        
#     def tearDown(self):
#         User.objects.all().delete()
#         Profile.objects.all().delete()
class PostTest(TestCase):
    def setUp(self):
        self.hood = Neighborhood(name= "hood1")
        self.user = User(username = "vic")
        self.hood.save()
        self.post = Post(user= self.user,description= "hello", hood =  self.hood , image = "jpg",pub_date = "22/2/22",  )
        self.post.save_post()
    def test_instance(self):
        self.assertEqual(self.post, Post )
    
    def test_save_method(self):
        self.post.save()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
    def test_delete_method(self):
        self.post.delete_project()
        posts = Post.objects.all()
        self.assertTrue(len(posts) == 0)
        
    def tearDown(self):
        Post.objects.all().delete()

class HoodTest(TestCase):
    def setUp(self):
        self.hood = Neighborhood(name= "garden" ,location= "almasi", health_contact = 77,police_contact = 333, image = "jpg"  )
        self.hood.save_hood()
    def test_instance(self):
        self.assertEqual(self.hoood, Neighborhood )
    
    def test_save_method(self):
        self.hood.save()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) > 0)
    def test_delete_method(self):
        self.post.delete_hood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) == 0)
        
    def tearDown(self):
        Neighborhood.objects.all().delete()