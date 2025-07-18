from relationship_app.models import *

# query books by a given author
books = author_instance.books.get(name)

# list all books in library
books = Book.objects.all()

# librarian for library
librarian = library_instance.librarian.get(name)