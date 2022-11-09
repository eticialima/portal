from django.urls import path  
from home import views, likes_comments 
  
app_name="home" 
urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),

	path('post-detail/<int:pk>/', views.DetailView.as_view(), name='post-detail'),  

	path('tags/<slug:tag_slug>/', views.TagIndexView.as_view(), name='tagged'),   

	path('category/<int:cat_slug>/', views.CategoryFilterView.as_view(), name='category'),

	path('post/<int:pk>/like', likes_comments.AddLike.as_view(), name='like'),

	path('post/<int:pk>/dislike', likes_comments.AddDislike.as_view(), name='dislike'), 

	path('post/<int:post_pk>/comment/delete/<int:pk>/', likes_comments.CommentDeleteView.as_view(), name="comment-delete"),

	path('post/<int:post_pk>/comment/edit/<int:pk>/', likes_comments.CommentEditView.as_view(), name="comment-edit"),
	
	path('post/<int:post_pk>/comment/<int:pk>/like', likes_comments.AddCommentLike.as_view(), name="comment-like"),
	
	path('post/<int:post_pk>/comment/<int:pk>/dislike', likes_comments.AddCommentDislike.as_view(), name="comment-dislike"),
	
	path('post/<int:post_pk>/comment/<int:pk>/reply',likes_comments.CommentReplyView.as_view(), name='comment-reply'),
] 