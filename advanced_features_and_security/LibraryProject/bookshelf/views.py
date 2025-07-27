from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import permission_required,login_required
from bookshelf.models import Book
from django.contrib import messages
from .forms import ExampleForm

# Create your views here.
@login_required
@permission_required('bookshelf.view_book',raise_exception=True)
def book_list(request):
    """View all books - requires view_book permission"""
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        #book.isbn = request.POST.get('isbn', book.isbn)
        book.save()

        messages.success(request, f'Book "{book.title}" updated successfully!')
        return redirect('book-list')
    return render(request, 'books/edit.html', {'book': book})


@login_required
@permission_required('bookshelf.delete_book', raise_exception=True)
def delete_book(request, book_id):
    """Delete book - requires delete_book permission"""
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        title = book.title
        book.delete()
        messages.success(request, f'Book "{title}" deleted successfully!')
        return redirect('book-list')

    return render(request, 'books/confirm_delete.html', {'book': book})


@login_required
@permission_required('bookshelf.add_book', raise_exception=True)
def add_book(request):
    """Add new book - requires add_book permission"""
    if request.method == 'POST':
        # Handle form submission
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')

        book = Book.objects.create(
            title=title,
            author=author,
            #isbn=isbn,
            created_by=request.user
        )
        messages.success(request, f'Book "{book.title}" added successfully!')
        return redirect('book-list')

    return render(request, 'books/add.html')

class FormView(ExampleForm):
    pass
