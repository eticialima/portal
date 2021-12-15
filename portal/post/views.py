from django.db.models.fields import SlugField
from django.urls import reverse_lazy
from django.contrib import messages 
from base.base_admin_permissions import BaseAdminUsersall 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.views.generic import ListView 
from post.models import *
from post.forms import PostForm 
from accounts.models import CustomUser 
from django.shortcuts import redirect, render, get_object_or_404  

from taggit.models import Tag
from django.template.defaultfilters import slugify
 
class IndexPostView(BaseAdminUsersall, TemplateView):
    template_name = 'post/index-post.html'
 
class PostView(BaseAdminUsersall, ListView):
    model = Post
    template_name = 'post/post.html'  
  
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['post_list'] = self.model.objects.all()  
    #     return context
 
class PostCreate(BaseAdminUsersall, CreateView):
    model = Post 
    form_class = PostForm 
    template_name = 'post/post_create.html' 

    def get(self, request): 
        form = PostForm() 
        posts = Post.objects.all()
        common_tags = Post.tags.most_common()[:4] 
        context = { 'posts':posts, 'common_tags':common_tags, 'form':form}  
        return render(request, self.template_name, context)
      
    def post(self, request, *args, **kwargs):  
        user_pk = request.user
        user = CustomUser.objects.filter(username=user_pk) 
        form = PostForm(request.POST, request.FILES)  

        if 'btn_adicionar':
            if form.is_valid(): 
                form_model = form.save(commit=False)
                form_model.slug = slugify(form_model.title)
                form_model.author = user[0]  
                form_model.save()
                form.save_m2m()
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
       
        
# class TagCreate(BaseAdminUsersall, TemplateView): 
#     template_name = 'home/home.html' 
  
    # def get_context_data(self, pk): 
    #     tag = get_object_or_404(Tag, pk=pk)
    #     common_tags = Post.tags.most_common()[:4]
    #     posts = Post.objects.filter(tags=tag)
    #     context = {
    #         'tag':tag,
    #         'common_tags':common_tags,
    #         'posts':posts,
    #     }
    #     return context 
 
 
