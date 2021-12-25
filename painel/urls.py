from django.urls import path
from painel.views import (IndexPainelView, PainelView)


urlpatterns = [
	path('', IndexPainelView.as_view(), name='index-painel'),
	path('painel/', PainelView.as_view(), name='painel'), 
] 