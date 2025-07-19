from relationship_app.models import *

# list all books in library
library =  Library.objects.get(name = library_name)
books = Book.objects.all()