from django.contrib import admin
from codepub.models import Post, LikePost, FollowAccount, PostComment, Report

admin.site.register((FollowAccount,PostComment, Report,LikePost,Post))

# Register your models here.
