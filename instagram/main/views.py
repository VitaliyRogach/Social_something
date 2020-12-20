from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView, LogoutView


class SignUpView(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')
    template_name = 'main/registration.html'


class SignInView(LoginView):
    model = User
    form_class = LoginUserForm
    success_url = reverse_lazy('main')
    template_name = 'main/sign.html'


def signview(request):
    return render(request, 'main/sign.html')

def registration(request):

    return render(request, 'main/registration.html')

def main_page(request):

    return render(request, 'main/main.html')