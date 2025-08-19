from django import forms
from .models import Post,CustomUser,Comment
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): #automatically gets username, password
    email = forms.EmailField()
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields('bio','avatar',)

    def save(self, commit=True): # save to db immediately
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'author', 'image')

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        category = cleaned_data.get('category')
        author = cleaned_data.get('author')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'author', 'post')

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')
        post = cleaned_data.get('post')
        comment = cleaned_data.get('comment')



