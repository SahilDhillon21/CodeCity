from django.contrib import admin
from django.urls import path
from vjti import views

urlpatterns = [
    path('vhome',views.vhome,name='vhome'),
]
