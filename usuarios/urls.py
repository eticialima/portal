from django.urls import path
from usuarios.views import (IndexUsuariosView)


urlpatterns = [
	path('', IndexUsuariosView.as_view(), name='index-usuarios'), 
] 