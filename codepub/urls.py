from django.contrib import admin
from django.urls import path
from codepub import views

urlpatterns = [
    path('codepub',views.codepubHome,name='codepubHome'),
    path('profile',views.profile,name='profile'),
    path('like-post',views.like_post,name='like-post'),
    path('follow/<str:F>',views.follow,name='follow'),
    path('view-profile/<str:pk>',views.view_profile,name='view-profile'),
    path('search',views.search,name='search'),
    path('post-comment',views.postComment,name='postComment'),
    path('report/<user_id>/<post_id>',views.report, name='report'),
    path('report-submitted',views.report_submitted, name='report-submitted'),
]
