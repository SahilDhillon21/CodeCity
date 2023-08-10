from django.contrib import admin
from codepub.models import Post, LikePost, FollowAccount, PostComment, Report

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register((FollowAccount,PostComment, Report))

# Register your models here.
