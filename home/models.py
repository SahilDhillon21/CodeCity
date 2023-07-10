from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Message from '+ self.name
    
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    citizenID = models.IntegerField()
    email = models.EmailField(max_length=100)
    bio = models.TextField(max_length=1000, blank=True)
    profileimg = models.ImageField(upload_to='profile_images',default='Default-avatar.jpg')
    location = models.CharField(max_length=100,blank=True)
    attendants = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
