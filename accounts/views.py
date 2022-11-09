from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.urls.base import reverse 
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView)
from base.base_admin_permissions import BaseAdminUsersAd, BaseAdminUsersall
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView 
from accounts.models import CustomUser

class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home:home')
        else:
            return self.render_to_response(self.get_context_data())


class UserCreate(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/user-new.html'
    success_url = reverse_lazy('accounts:login')


class UserChange(BaseAdminUsersall, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/user-change.html'
    success_url = reverse_lazy('profile:users-profile')
    success_message = 'Your profile change was successful' 


class UserDelete(BaseAdminUsersAd, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('profile:users-profile')
    template_name = 'accounts/user-delete.html'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('profile:users-profile')


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('accounts:login')
    success_message = 'Your password change was successful'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    success_message = 'Your password has been correctly reset. Login to get started'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'accounts/password-reset-complete.html'
    success_message = 'Your password has been correctly reset. Login to get started'

    def get(self, request, *args, **kwargs):
        return redirect('accounts:login') 
    

class TimeOutView(TemplateView):
    template_name = 'timeout/timeout.html'