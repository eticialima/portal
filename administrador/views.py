from django.views.generic.base import TemplateView
from django.views.generic.list import ListView  
from base.base_admin_permissions import BaseAdminUsersAd 

class IndexAdministradorView(BaseAdminUsersAd, TemplateView):
	template_name = 'administrador/index-administrador.html' 