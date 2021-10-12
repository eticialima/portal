from django.urls import path
from administrador.views import (IndexAdministradorView)


urlpatterns = [
	path('', IndexAdministradorView.as_view(), name='index-administrador'), 
] 