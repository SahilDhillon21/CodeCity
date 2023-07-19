from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    user =  models.CharField(max_length=100)       
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField(max_length=15000)
    created_at = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
