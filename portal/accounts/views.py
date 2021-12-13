from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from base.base_admin_permissions import BaseAdminUsersAd, BaseAdminUsersall
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView as TemplateView
from accounts.models import CustomUser
from django.views.generic import ListView
from django.contrib.auth.views import (
    LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView) 
import painel.urls

  
class UserLogin(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index-administrador')
        else:
            return self.render_to_response(self.get_context_data())




class UserCreate(SuccessMessageMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreateForm
    template_name = 'accounts/user-new.html'
    success_url = reverse_lazy('users')

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     username = request.POST.get('username')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     type_user = request.POST.get('type_user')
    #     is_active = request.POST.get('is_active')
    #     print(is_active)
    #     sendmail_rh(username,first_name,last_name,type_user)
    #     print("UserCreate Email Teste")
    #     return super().post(request, *args, **kwargs)


class UserChange(BaseAdminUsersAd, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/user-change.html'
    success_url = reverse_lazy('users')
    success_message = 'Sua mudança de perfil foi bem-sucedida' 

    # def get(self, request, *args, **kwargs):
    #     self.object = None
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.object = None
    #     username = request.POST.get('username')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     type_user = request.POST.get('type_user')
    #     is_active = request.POST.get('is_active', False)
    #     print(is_active)
    #     print(request.method)

    #     if 'is_active' in request.POST: #
    #         if is_active == False:
    #             print("Usuario já esta cadastrado no sistema.")
    #         else:
    #             sendmail_user(username,first_name,last_name,type_user)
    #             print("UserChange Email Teste")

    #     return super().post(request, *args, **kwargs)


class UserDelete(BaseAdminUsersAd, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('users')
    template_name = 'accounts/user-delete.html'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('users')


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/password-change.html'
    success_url = reverse_lazy('login')
    success_message = 'Sua mudança de senha foi bem sucedida'


class PasswordReset(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password-reset.html'


class PasswordResetConfirm(SuccessMessageMixin, PasswordResetConfirmView):
    success_message = 'Sua senha foi redefinida corretamente. Faça login para começar'


class PasswordResetComplete(SuccessMessageMixin, PasswordResetCompleteView):
    template_name = 'accounts/password-reset-complete.html'
    success_message = 'Sua senha foi redefinida corretamente. Faça login para começar'

    def get(self, request, *args, **kwargs):

        return redirect('login')


class UserListView(BaseAdminUsersAd, ListView):
    model = CustomUser
    template_name = 'accounts/usuarios.html'


class TimeOutView(TemplateView):
    template_name = 'timeout/timeout.html'


class UserProfileUpdateView(BaseAdminUsersall ,UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'accounts/user-profile.html'
    success_url = reverse_lazy('painel')
    success_message = 'Seus dados foram alterados com sucesso'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(*args, **kwargs)
        return context

 