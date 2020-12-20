from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': "Email"}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Username"}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': "Password"}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': "Repeat password"}))
    error_messages = UserCreationForm.error_messages
    error_messages['password_mismatch'] = 'Password incorrect.'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    error_messages = AuthenticationForm.error_messages
    error_messages['invalid_login'] = 'Enter a true login and password'

    class Meta:
        model = User
        fields = ['username', 'password']