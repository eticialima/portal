from django.urls import path
from post.views import (IndexPostView, PostView, PostCreate)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', IndexPostView.as_view(), name='index-post'),
	path('post/', PostView.as_view(), name='post'), 
	path('post-create/', PostCreate.as_view(), name='post-create'),  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)