from django.urls import path
from . import views
from .views import chat_view
from .views import register_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('testimonies/', views.testimonies, name='testimonies'), 
    path('gallery/', views.gallery, name='gallery'),  
    path('faq/', views.faq, name='faq'),  
    path('contact-us/', views.contact_us, name='contact_us'), 
    path('login/', views.login_view, name='login'),  
    path('register/', views.register_view, name='register'),  
    path('userdash/', views.dashboard, name='userdash'),
    path('chat/', chat_view, name='chat'),
    path('reflect/', views.reflect, name='reflect'),
    path('post/', views.post, name='post'),
    path('save_post/', views.save_post, name='save_post'),
    path('get-posts/', views.get_posts, name='get_posts'),
    path('logout/', views.logout_view, name='logout'),
]

