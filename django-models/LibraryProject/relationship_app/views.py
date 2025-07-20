from django.shortcuts import render
from bookshelf.models import Book
from django.views.generic import ListView
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'list_books.html',context)

class BookList(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'list_book.html'

