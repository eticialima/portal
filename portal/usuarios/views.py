from django.views.generic.base import TemplateView  
from base.base_admin_permissions import BaseAdminUsersall

class IndexUsuariosView(BaseAdminUsersall, TemplateView):
	template_name = 'usuarios/index-usuarios.html'