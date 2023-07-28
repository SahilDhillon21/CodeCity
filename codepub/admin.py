from django.contrib import admin
from codepub.models import Post, LikePost, FollowAccount, PostComment

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register((FollowAccount,PostComment))

# Register your models here.
