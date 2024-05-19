from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'deadline']  


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
