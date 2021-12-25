from django.urls import path 
from post.views import (IndexPostView, PostView, PostCreate, PostUpdate ) 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
	path('', IndexPostView.as_view(), name='index-post'),
	path('post/', PostView.as_view(), name='post'), 
	path('post-create/', PostCreate.as_view(), name='post-create'),  

	# path('tags/', TagCreate.as_view(), name='tags'),  
 	# path('tags/<slug:slug>/', TagIndexView.as_view(), name='post_by_tag'),   
	#path('tag/<int:pk>/', TagCreate.as_view(), name="tagged"),
	
	path('<int:pk>/post-update/', PostUpdate.as_view(), name='post-update'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)