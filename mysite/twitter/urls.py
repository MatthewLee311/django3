from django.urls import path
from django.contrib import admin
from . import views

app_name = 'twitter'
urlpatterns = [
    path('', views.login),
    path('', views.index),
    path('getPost', views.get_post),
]
