from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView

from core.forms import RegisterUserForm, ProfileUserForm


class RegisterUserView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterUserForm

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class LoginUserView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('index')


class LogoutUserView(LogoutView):
    template_name = 'logout.html'

    def get_success_url(self):
        return reverse('login')


class ProfileView(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = ProfileUserForm

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Edit user data'
        return context