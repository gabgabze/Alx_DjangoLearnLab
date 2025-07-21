from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import render,redirect
from .models import Library,Book
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from decorators import is_librarian,is_admin,is_member
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

""" create role views"""
#@user_passes_test(is_admin)
def admin_view(request):
    context ={}
    return render(request,'relationship_app/admin_view.html',context)

#@user_passes_test(is_librarian)
def librarian_view(request):
    context = {}
    return render(request,'relationship_app/librarian_view.html',context)

#@user_passes_test(is_member)
def member_view(request):
    context = {}
    return render(request,'relationship_app/member_view.html',context)