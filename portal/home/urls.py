from django.urls import path
from django.views.generic.base import TemplateView
from home.views import (IndexHomelView, HomeView, DetailView)
from home.forms import ShareForm

from django.urls import path
from home.views import ( 
    AddDislike, 
    AddLike, 
    CommentDeleteView, 
    CommentEditView, 
    CommentReplyView,
    AddCommentDislike, 
    AddCommentLike,
    SharedPostView 
    )

app_name="home"
urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('index-home/', IndexHomelView.as_view(), name='index-home'), 
	path('post-detail/<int:pk>/', DetailView.as_view(), name='post-detail'), 
	
	path('post/<int:pk>/like', AddLike.as_view(), name='like'),
	path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
	path('post/<int:pk>/share', SharedPostView.as_view(), name='share-post'),
	
	path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name="comment-delete"),
	path('post/<int:post_pk>/comment/edit/<int:pk>/', CommentEditView.as_view(), name="comment-edit"),
	path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name="comment-like"),
	path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name="comment-dislike"),
	path('post/<int:post_pk>/comment/<int:pk>/reply',CommentReplyView.as_view(), name='comment-reply'),
] 






 
