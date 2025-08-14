from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django_blog.settings import AUTH_USER_MODEL


# Create your models here.
# create custom user
class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)