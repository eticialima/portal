from django.db.models import Q
from django.shortcuts import render  
from django.core.paginator import Paginator 
from django.views.generic.base import TemplateView 
from django.views.generic import DetailView, ListView 
from post.models import *
from post.forms import *
from home.forms import *   

class IndexHomelView(TemplateView):
    template_name = 'home/index-home.html' 
 
class HomeView(ListView):
    model = Post 
    template_name = 'home/home.html'   
    paginate_by = 2 
  
    def get_queryset(self):      
        title = self.request.GET.get('title')
        if title:  
            post_list = self.model.objects.filter(title__icontains=title) 
        else:
            post_list = self.model.objects.filter() 
        return post_list  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()  
        context['category'] = Category.objects.all() 
        return context
    
  
class DetailView(DetailView):
    model = Post 
    template_name = 'home/post_detail.html' 
    
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = SocialCommentForm() 
        comments = SocialComment.objects.filter(post=post).order_by('-created_on')
        post_list = self.model.objects.all()[:5] 
        
        context = {
            'post': post,
            'form': form,
            'comments':comments,  
            'post_list': post_list,
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
  
 
class TagIndexView(ListView):
    model = Post
    template_name = 'home/home.html'   
    context_object_name = 'post_list' 
    
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['tag_slug'])

