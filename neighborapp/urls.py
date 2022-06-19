from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.home , name='home'),
    path('', views.hood , name='hood'),
    path('neighborhood/<int:hood_id>', views.each_hood, name='each_hood'),  
    path('profile/<username>', views.profile, name='profile'),
    path('new/post', views.new_post, name='newpost'),
    path('profile/<username>/settings', views.update_profile, name='update_profile'),
    path('profiles/<username>/profile/', views.show_profile, name='show_profile'),  
    path('business/<bizname>', views.show_business, name='show_business'),
    path('search', views.search_biz, name='search'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)