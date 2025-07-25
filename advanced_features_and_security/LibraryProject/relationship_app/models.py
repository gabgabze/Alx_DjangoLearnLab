from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your user model
USER_ROLES =[
    ('Admin','Admin'),
    ('Librarian','Librarian'),
    ('Member','Member')
]
"""create customUser"""
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to='profile_photos')

    """create custom user manager"""
    def create_user(self, email,date_of_birth,profile_photo, password=None, **extra_fields):
        self.date_of_birth = date_of_birth
        self.profile_photo = profile_photo
        self.email = email

    def create_superuser(self, email,date_of_birth,profile_photo, password=None, **extra_fields):
        self.date_of_birth = date_of_birth
        self.profile_photo = profile_photo
        self.email = email

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='profile')
    role = models.CharField(max_length=100, choices=USER_ROLES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
        #return str(self.user)

# Author model
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Book'
        permissions = ('can_add_book','can_change_book','can_delete_book')

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)