from django.db import models
from django.contrib.auth.models import AbstractUser

from social_media_api import settings


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)
    followers = models.ManyToManyField(symmetrical=False, related_name='follower', to=settings.AUTH_USER_MODEL)
