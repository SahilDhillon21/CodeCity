from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    user =  models.CharField(max_length=100)       
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(max_length=15000)
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.user+" - "+self.title
    
class LikePost(models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username+" liked "+self.post_id
    
class FollowAccount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.follower +" follows "+self.user
    
class PostComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username+" commented "+self.comment
    
    def isLiked(self):
        return self.liked


    

