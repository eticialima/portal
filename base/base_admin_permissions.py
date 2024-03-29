from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View


class BaseAdminUsers(
	LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, View):
	"""
	Base class for test if user type_user have authorized access to
	admin functions.
	And display sucess messages
	"""
	authorized_admin_access = []

	def test_func(self):
		"""
		Test if authenticated user can access to this view.
		"""

		if self.request.user.type_user in self.authorized_admin_access:
			return True

	def handle_no_permission(self):
		"""
		Redirect if authenticated user can not access to this view.
		"""
		if self.raise_exception or self.request.user.is_authenticated:
			return redirect('painel')

		return redirect('accounts:login')


class BaseAdminUsersAd(BaseAdminUsers):
	"""
	type_user authorized to access admin functions.
	- Administrator 
	"""
	authorized_admin_access = ['ad', 'co']

class BaseAdminUsersall(BaseAdminUsers):
	"""
	type_user authorized to access admin functions.
	- User
	"""
	authorized_admin_access = ['ad', 'co', 'us']


if __name__ == '__main__':
	pass
