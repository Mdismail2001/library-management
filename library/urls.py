from django.urls import path
from . import views



urlpatterns = [
    path('', views.register, name= 'register'),
    path('signup/', views.signup , name='signup'),
    path('home/', views.home, name= 'home'),
    path('about/', views.about, name='about'),
    
]
