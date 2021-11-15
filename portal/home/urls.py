from django.urls import path
from django.views.generic.base import TemplateView
from home.views import (IndexHomelView, HomeView, DetailView)

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('index-home/', IndexHomelView.as_view(), name='index-home'), 
	path('post-detail/<int:pk>/', DetailView.as_view(), name='post-detail') 
] 