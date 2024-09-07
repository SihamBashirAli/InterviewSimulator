# accounts/urls.py

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    
]
#from .views import login_view, logout_view, register_view

#path('login/', login_view, name='login'),
    #path('logout/', logout_view, name='logout'),
    #path('register/', register_view, name='register'),

