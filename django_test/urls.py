
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('form',views.create,name='create'),
    path('index', views.index),
    path('smartphone.html/',views.Smartphone,name='mobile'),
    path('laptop.html/',views.laptop,name='laptop'),
    path('watches.html/',views.watch,name='watch'),
    path('headphones.html/',views.headphone,name='headphone'),
]