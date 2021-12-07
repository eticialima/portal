from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.base import TemplateView,View 
from django.views.generic import DetailView, ListView 
from post.models import *
from post.forms import *
from home.forms import *
from .filters import PostFilter
  
class IndexHomelView(TemplateView):
    template_name = 'home/index-home.html' 
 
class HomeView(ListView):
    model = Post 
    template_name = 'home/home.html' 
  
    def get_context_data(self, **kwargs):    
        context = super().get_context_data(**kwargs)  
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset()) 
        context['has_filter'] = any(field in self.request.GET for field in set(context['filter'].get_fields())) 
        return context
        
class DetailView(DetailView):
    model = Post 
    template_name = 'home/post_detail.html' 
    
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = SocialCommentForm() 
        comments = SocialComment.objects.filter(post=post).order_by('-created_on')
        filter = PostFilter(self.request.GET, queryset=self.get_queryset())
        tag_list = Tag.objects.all()
        post_list = self.model.objects.all()[:5] 
        context = {
            'post': post,
            'form': form,
            'comments':comments,
            'filter': filter,
            'tag_list': tag_list,
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
  
class AddLike(LoginRequiredMixin,View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False
        
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next) 


class AddDislike(LoginRequiredMixin,View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False
        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = SocialComment.objects.get(pk=pk)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next) 

class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = SocialComment.objects.get(pk=pk)

        is_like = False
        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False
        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        

class CommentReplyView(LoginRequiredMixin, View):
    def post(self, request, post_pk, pk, *args, **kwargs):
        post=Post.objects.get(pk=post_pk)
        parent_comment = SocialComment.objects.get(pk=pk)
        form=SocialCommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        return redirect('home:post-detail', pk=post_pk)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialComment
    template_name="home/comments/comment_delete.html"

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('home:post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class CommentEditView(UpdateView):
    model = SocialComment
    fields = ['comment']
    template_name = 'home/comments/comment_edit.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('home:post-detail', kwargs={'pk':pk})


