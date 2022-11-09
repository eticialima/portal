from django.urls import path 
from post import views

urlpatterns = [  
	path('post/', views.PostView.as_view(), name='post'), 

	path('post-create/', views.PostCreate.as_view(), name='post-create'),

	path('<int:pk>/post-update/', views.PostUpdate.as_view(), name='post-update'), 
  
 	path('<int:pk>/post-delete/', views.PostDelete.as_view(), name='post-delete'), 
]