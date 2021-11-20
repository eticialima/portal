from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from base.base_admin_permissions import BaseAdminUsersAd, BaseAdminUsersall
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from post.models import *
from post.forms import PostForm
from accounts.models import CustomUser


class IndexPostView(BaseAdminUsersall, TemplateView):
    template_name = 'post/index-post.html'


class PostView(BaseAdminUsersall, ListView):
    model = Post
    template_name = 'post/post.html'   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.model.objects.all()  
        return context


class PostCreate(BaseAdminUsersall, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    # success_url = reverse_lazy('post')

    # cadastra post para user selecionado
    def post(self, request, *args, **kwargs):
        user_pk = request.user
        user = CustomUser.objects.filter(username=user_pk)
        # form = self.get_form()
        form = PostForm(request.POST, request.FILES)
        # no formulario tem propriedade "btn_adicionar" quando adiciona o formulario roda if abaixo.
        if 'btn_adicionar':
            if form.is_valid():
                form_model = form.save(commit=False)
                form_model.author = user[0]
                form_model.save()
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def get_success_url(self) -> str:
        messages.success(self.request, 'O post foi Cadastrado com sucesso')
        return reverse_lazy('post')
 
class PostUpdate(BaseAdminUsersall, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_update.html'
    success_url = reverse_lazy('post')
    success_message = 'O post foi Atualizado com sucesso'