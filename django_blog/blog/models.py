from django.db import models
from  django.contrib.auth.models import User
from django.conf import settings
#from django_blog.settings import AUTH_USER_MODEL


# Create your models here.
# create custom user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/')


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)