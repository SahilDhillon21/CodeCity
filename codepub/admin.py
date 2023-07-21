from django.contrib import admin
from codepub.models import Post, LikePost, FollowAccount

admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowAccount)

# Register your models here.
