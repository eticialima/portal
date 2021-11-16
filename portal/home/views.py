from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from base.base_admin_permissions import BaseAdminUsersall
from post.models import *
from post.forms import *
from .filters import PostFilter

class IndexHomelView(TemplateView):
    template_name = 'home/index-home.html'
 
class HomeView(ListView):
    model = Post 
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        f = PostFilter(self.request.GET, queryset=Post.objects.all()) 
        context = super().get_context_data(**kwargs)  
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        context['has_filter'] = any(field in self.request.GET for field in set(f.get_fields()))
        return context
     

class DetailView(DetailView):
    model = Post 
    template_name = 'home/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['post_list'] = self.model.objects.all()[:5]
        context['tag_list'] = Tag.objects.all() 
        context['has_filter'] = any(field in self.request.GET for field in set(context['filter'].get_fields()))
        return context
 