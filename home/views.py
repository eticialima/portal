from typing import ContextManager
from django.shortcuts import render 
from django.views.generic import DetailView, ListView 
from post.models import Post, Category, SocialComment
from post.forms import PostForm
from home.forms import SocialCommentForm  

class HomeView(ListView):
    model = Post 
    template_name = 'home/home.html'   
    paginate_by = 8
  
    def get_queryset(self):      
        title = self.request.GET.get('title')
        if title:  
            post_list = self.model.objects.filter(title__icontains=title, author__is_active__exact=True) 
        else:
            post_list = self.model.objects.filter(author__is_active__exact=True) 
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
        post_list = self.model.objects.filter(author__is_active__exact=True)[:5]
        cat = Category.objects.all()
        
        context = {
            'post': post,
            'form': form,
            'comments':comments,  
            'post_list': post_list,
            'cat':cat,
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
    
    
class CategoryFilterView(ListView):
    model = Post
    template_name = 'home/home.html'    
    
    def get_queryset(self):
        return Post.objects.filter(category__pk=self.kwargs['cat_slug'], author__is_active__exact=True)