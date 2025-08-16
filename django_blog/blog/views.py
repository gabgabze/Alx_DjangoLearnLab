from lib2to3.fixes.fix_input import context
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Comment
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm

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

# CBV views for the post
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        pass

class PostCreateView(CreateView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_create.html'


#@login_required(login_url='/login/')
#@user_passes_test(lambda u: u.is_authenticated())
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_update.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True


#@login_required
#@user_passes_test(lambda u:(u,))
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True



# comment form View

class CommentListView(ListView):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-date_posted']

class CommentDetailView(DetailView):
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name = 'comment'
    def get_context_data(self, **kwargs):
        pass
class CommentCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'blog/comment_create.html'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.is_staff:
            return True

class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    context_object_name = 'comment'
    template_name = 'blog/comment_update.html'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.is_staff:
            return True

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Comment
    context_object_name = 'comment'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author or self.request.user.is_staff:
            return True