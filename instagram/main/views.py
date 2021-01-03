
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.models import User
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView
from .models import Profile


class SignUpView(CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')
    template_name = 'main/registration.html'


class SignInView(LoginView):
    model = User
    form_class = LoginUserForm
    success_url = reverse_lazy('signup')
    template_name = 'main/sign.html'


class UserProfile(DetailView):
    model = Profile
    slug_field = "slug"
    context_object_name = "profile"
    template_name = 'main/profile.html'

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs.get('slug'))


def ProfileUser(request):
    return render(request, 'main/profile.html')


def signview(request):
    return render(request, 'main/sign.html')


def registration(request):
    return render(request, 'main/registration.html')


def main_page(request):
    return render(request, 'main/main.html')