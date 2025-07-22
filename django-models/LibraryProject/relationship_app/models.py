from django.db import models
from django.contrib.auth.models import User

# Create your user model
USER_ROLES =[
    ('Admin','Admin'),
    ('Librarian','Librarian'),
    ('Member','Member')
]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
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
        model = 'books'
        permissions = ('can_add_book','can_change_book','can_delete_book')

class Library(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)


class Librarian(models.Model):
    name = models.CharField(max_length=50)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)