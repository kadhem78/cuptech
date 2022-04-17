from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name='home'),
    path('posts/<slug:slug>' , views.post_details , name='post_details'),
    path('manage/' , views.manage , name='manage'),
    path('create/' , views.create_post , name='create_post'),
    path('update/<slug:slug>' , views.update_post , name='update_post'),
    path('delete/<slug:slug>' , views.delete_post , name='delete_post'),
]
