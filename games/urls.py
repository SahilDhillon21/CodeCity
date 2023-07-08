from django.contrib import admin
from django.urls import path
from games import views

urlpatterns = [
    path('cvgames/',views.cvgames,name='cvgames'),
    path('cvgames/airhockeySummary',views.airhockeySummary,name='airhockeySummary'),
    path('cvgames/airhockeyPlay',views.airhockeyPlay,name='airhockeyPlay'),
]
