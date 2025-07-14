## To retrieve data ##
from bookshlef.models import Book

book1 = Book.objects.get(title="1984")

