from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView,DetailView
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/list_books.html',context)

class BookDetail(DetailView):
    model = Book
    context_object_name = 'books'
    template_name = 'relationship_app/library_detail.html'

