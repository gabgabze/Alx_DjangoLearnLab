## import the app model ##
from bookshelf.models import Book

book1 = Book.objects.create(title="19984",author="George Orwell", year_published=1949)