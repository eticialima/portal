from django.views.generic.base import TemplateView  
from base.base_admin_permissions import BaseAdminUsersAd

class IndexAdministradorView(BaseAdminUsersAd, TemplateView):
	template_name = 'administrador/index-administrador.html'