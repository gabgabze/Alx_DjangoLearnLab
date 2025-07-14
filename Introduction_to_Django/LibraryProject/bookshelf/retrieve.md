## To retrieve data ##
from bookshlef.models import Book

book1 = Book.objects.all()

print(book1)