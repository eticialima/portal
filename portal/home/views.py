from django.shortcuts import get_object_or_404, render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView,View 
from django.views.generic import DetailView, ListView
from taggit.models import Tag 
from post.models import *
from post.forms import *
from home.forms import *
from .filters import PostFilter 

from taggit.models import Tag
from django.template.defaultfilters import slugify


class IndexHomelView(TemplateView):
    template_name = 'home/index-home.html' 
 
class HomeView(ListView):
    model = Post 
    template_name = 'home/home.html'   
 
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

    # def get_context_data(self, **kwargs):    
    #     context = super().get_context_data(**kwargs)    
    #     context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
    #     context['has_filter'] = any(field in self.request.GET for field in set(context['filter'].get_fields()))  
    #     return context
        
class DetailView(DetailView):
    model = Post 
    template_name = 'home/post_detail.html' 
    
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = SocialCommentForm() 
        comments = SocialComment.objects.filter(post=post).order_by('-created_on')
        filter = PostFilter(self.request.GET, queryset=self.get_queryset())
      
        post_list = self.model.objects.all()[:5] 
        context = {
            'post': post,
            'form': form,
            'comments':comments,
            'filter': filter,
 
            'post_list': post_list,
            'has_filter': any(field in self.request.GET for field in set(filter.get_fields()))  
        }  
        return render(request, 'home/post_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = SocialCommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()

        comments = SocialComment.objects.filter(post=post).order_by('-created_on')

        context = {
            'post': post,
            'form': form,
            'comments':comments
        }

        return render(request, 'home/post_detail.html', context)
  
 
# class TagIndexView(ListView):
#     model = Post
#     template_name = 'home/home.html'   
#     context_object_name = 'post_list'
  
#     def context_data(self): 
#         return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))