from relationship_app.models import *

# query books by a given author
#books = Book.objects.filter(author=author)

# list all books in library#
library = Library.objects.get(name=library_name)
books = library.book.all()


# books = Book.objects.filter(library=library)

# librarian for library
#librarian = Library.library