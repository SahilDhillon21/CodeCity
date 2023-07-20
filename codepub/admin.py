from django.contrib import admin
from codepub.models import Post, LikePost

admin.site.register(Post)
admin.site.register(LikePost)

# Register your models here.
