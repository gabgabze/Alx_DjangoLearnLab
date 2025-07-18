from django.db import models

# Create your models here.

# Author model
class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,verbose_name='books' on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField(Book, verbose_name="library")


class Librarian(models.Model):
    name = CharField(max_length=50)
    library = models.OneToOneField(Library, verbose_name='librarian', on_delete=models.CASCADE)