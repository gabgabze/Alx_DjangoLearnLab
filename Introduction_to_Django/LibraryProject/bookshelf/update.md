from bookshelf.models import Book

book1 = Book.objects.get(title ="1984")
book1.title = "1985"
book1.save()