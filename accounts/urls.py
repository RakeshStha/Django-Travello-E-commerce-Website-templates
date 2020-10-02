from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register',views.register, name="register"),
    path('login',views.loginUser, name="login"),
    path('index',views.index,name="index"),
    path('logout',views.logout, name="logout")
]
