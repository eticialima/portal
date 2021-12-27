from django.urls import path 
from post.views import (PostView, PostCreate, PostUpdate) 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
	path('post/', PostView.as_view(), name='post'), 
	path('post-create/', PostCreate.as_view(), name='post-create'),   
	path('<int:pk>/post-update/', PostUpdate.as_view(), name='post-update'),  
]