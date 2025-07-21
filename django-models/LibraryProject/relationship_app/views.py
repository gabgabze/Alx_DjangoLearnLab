from django.shortcuts import render,redirect
from .models import Library,Book
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/list_books.html',context)

class LibraryDetailView(DetailView):
    model = Library
    context_object_name = 'books'
    template_name = 'relationship_app/library_detail.html'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
