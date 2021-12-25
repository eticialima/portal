from django.views.generic.base import TemplateView  
from base.base_admin_permissions import BaseAdminUsersAd

class IndexColaboradorView(BaseAdminUsersAd, TemplateView):
	template_name = 'colaborador/index-colaborador.html'