from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

"""create customUser"""
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photos')

    def __str__(self):
        return self.username



"""create custom user manager"""
class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth,profile_photo,password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email) # clean to have standardized email format
        user = self.model() # create user object
        user.set_password(password)
        user.date_of_birth = date_of_birth
        user.profile_photo = profile_photo
        user.email = email
        user.save()
        return user

    def create_superuser(self, email, date_of_birth,profile_photo,password,**extra_fields):
        user = self.create_user(email,date_of_birth,profile_photo,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class Editor(models.Model):
    name = models.CharField(max_length=100)
    #profile = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'
        ordering = ['name']
        permissions = [
            ('can_vew','can_create'),
            ('can_edit','can_delete')
        ]
