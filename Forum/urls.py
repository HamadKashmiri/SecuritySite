
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "forum-home"),
    path('register', views.register, name = "register"),
    path('login', views.loginpage, name = "login"),
    path('logout', views.logoutUser, name = "logout"),
    path('profile', views.profile, name = "profile")
        
]
