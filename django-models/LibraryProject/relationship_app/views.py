from django.shortcuts import render,redirect
from .models import Library,Book
from django.views.generic.detail import DetailView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request,'relationship_app/list_books.html',context)

class ibraryDetailView(DetailView):
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
    return render(request, 'accounts/register.html', {'form': form})


