from django.urls import path
from colaborador.views import (IndexColaboradorView)


urlpatterns = [
	path('', IndexColaboradorView.as_view(), name='index-colaborador'), 
] 