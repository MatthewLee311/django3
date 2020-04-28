from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.userLogin),
    path('twitter/', views.index),
    path('getPost', views.get_post),
]
