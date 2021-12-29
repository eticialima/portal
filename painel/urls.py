from django.urls import path
from painel.views import PainelView

urlpatterns = [ 
	path('painel/', PainelView.as_view(), name='painel'), 
] 