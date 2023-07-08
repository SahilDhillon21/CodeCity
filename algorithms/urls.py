from django.contrib import admin
from django.urls import path
from algorithms import views

urlpatterns = [
    path('huffmanIN/',views.huffmanIN,name='huffmanIN'),
    path('huffmanIN/huffmanOUT/',views.huffmanOUT,name='huffmanOUT'),
]