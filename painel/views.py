from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall
  
class PainelView(BaseAdminUsersall, TemplateView):
	template_name = 'painel/painel.html'
