"""fourpong URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
# from django.contrib.auth.models import User


from . import views

# username = user.username
# App Level URLs
urlpatterns = [
    path('', views.homePage),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('homePage/', views.homePage),
    path('leaderBoard/', views.leaderBoard),
    path('gameLobby/', views.gameLobby),
    path('getWins/', views.getWins),
    path('chat/', views.chatPage, name='index'),
    path('chat/<str:room_name>/', views.room, name='room')
]
