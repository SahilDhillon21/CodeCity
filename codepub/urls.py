from django.contrib import admin
from django.urls import path
from codepub import views

urlpatterns = [
    path('codepub',views.codepubHome,name='codepubHome'),
    path('profile',views.profile,name='profile'),
]
