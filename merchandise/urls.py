from django.contrib import admin
from django.urls import path, include
from merchandise import views

urlpatterns = [
    path('',views.merchhome,name='merchhome'),
]