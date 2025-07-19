from relationship_app.models import *

# list all books in library
library =  Library.objects.get(name = "Kitengela")
library.books.all()