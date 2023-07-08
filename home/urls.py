from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),



    path('algorithms',include("algorithms.urls")),
    path('games',include("games.urls")),
    path('merchandise',include("merchandise.urls")),
    path('codepub',include("codepub.urls")),
]