from lib2to3.fixes.fix_input import context

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from .models import Post
# Create your views here.
# register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = form.save(commit=False)
            user.username = username
            user.save()
    return render(request, 'blog/register.html', {'form': UserCreationForm})

# login view
def login(request):
    context ={
        'form':"form"
    }
    return render(request, 'blog/login.html',context)

# logout view
def logout(request):
    return render(request, 'blog/logout.html')

def profile(request):
    return render(request, 'blog/profile.html')