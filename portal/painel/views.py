from django.views.generic.base import TemplateView 
from base.base_admin_permissions import BaseAdminUsersall

class IndexPainelView(BaseAdminUsersall, TemplateView):
	template_name = 'painel/index-painel.html'

class PainelView(BaseAdminUsersall, TemplateView):
	template_name = 'painel/painel.html'
