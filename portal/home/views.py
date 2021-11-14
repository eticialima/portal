from django.shortcuts import render 
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from base.base_admin_permissions import BaseAdminUsersall
from post.models import Post
from post.forms import PostForm

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
		return context
