from relationship_app.models import *

# query books by a given author
book = author_instance.books.all()

# list all books in library
books = library_instance.books.all()

# librarian for library
librarian = library_instance.librarian.all()