
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subtopic/<str:pk>', views.subtopics, name='subtopic'),
    path('subtopic/post/<str:pk>', views.post, name='post'),
    path('post-form/<str:pk>', views.post_form, name='post-form'),
    path('update-post/<str:pk>', views.update, name='post-update'),
    path('delete-post/<str:pk>', views.delete, name='post-delete'),
    path('profile/', views.profile, name='profile'),
]
