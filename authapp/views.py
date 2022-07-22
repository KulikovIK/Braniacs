from typing import Any, Optional
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from authapp.models import User
from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _


class MyLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': _('User login')
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url: Optional[str] = reverse_lazy('authapp:login')


class MyLogoutView(LogoutView):
    pass


class EditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name: str = 'authapp/edit.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('authapp:edit')
      