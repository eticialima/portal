from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView as TemplateView

class IndexView(TemplateView):
	template_name = 'webpage/index.html'

class IndexManagerView(TemplateView):

	def get(self, request, *args, **kargs):
		"""
		After user login, redirect for respective dashboard,
		depending on the type_user
		"""

		type_user = {
			'ad': 'administrador',
			'co': 'colaborador',
			'us': 'usuarios', 
		}

		if request.user.is_authenticated:

			template = type_user[request.user.type_user]
			return redirect('index-{}'.format(template))

		else:
			return redirect('login') 

 