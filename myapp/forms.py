from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import student

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __str__(self):
        return self.username


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ('image', 'phone')



