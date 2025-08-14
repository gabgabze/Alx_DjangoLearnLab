from django import forms
from .models import Post,CustomUser
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm): #automatically gets username, password
    email = forms.EmailField()
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields('email', 'bio', 'avatar')

    def save(self, commit=True): # save to db immediately
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

