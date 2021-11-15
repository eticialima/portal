from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from base.base_admin_permissions import BaseAdminUsersall
from post.models import *
from post.forms import *


class IndexHomelView(TemplateView):
    template_name = 'home/index-home.html'


class HomeView(TemplateView):
    model = Post
    form_class = PostForm
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.model.objects.all() 
        return context


class DetailView(DetailView):
    model = Post
    form_class = PostForm
    template_name = 'home/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = self.model.objects.all()[:5]
        context['tag_list'] = Tag.objects.all() 
        return context
 