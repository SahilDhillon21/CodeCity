from django.contrib import admin
from django.urls import path
from codepub import views

urlpatterns = [
    path('codepub',views.codepubHome,name='codepubHome'),
    path('profile',views.profile,name='profile'),
    path('like-post',views.like_post,name='like-post'),
    path('view-profile/<str:pk>',views.view_profile,name='view-profile'),
]
