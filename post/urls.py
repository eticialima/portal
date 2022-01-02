from django.urls import path 
from post.views import (PostView, PostCreate, PostUpdate,PostDelete) 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [  
	path('post/', PostView.as_view(), name='post'), 
	path('post-create/', PostCreate.as_view(), name='post-create'),   
	path('<int:pk>/post-update/', PostUpdate.as_view(), name='post-update'), 
  
 	path('<int:pk>/post-delete/', PostDelete.as_view(), name='post-delete'), 
]