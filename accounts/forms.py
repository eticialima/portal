from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from accounts.models import CustomUser  

class CustomUserCreateForm(UserCreationForm): 
 
	class Meta():
		model = CustomUser
		fields = ('user_name','first_name', 'last_name', 'username', 'type_user', 'is_active')
		labels = {'username': 'Username/Email'}

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["username"] 
		print("create") 
		if commit:
			user.save() 
		return user 
 
class CustomUserChangeForm(UserChangeForm):

	class Meta():
		model = CustomUser
		fields = ('user_name', 'first_name', 'last_name', 'username', 'type_user', 'is_active')
		labels = {'username': 'Username/Email'}
 
	def save(self, commit=True):
		user = super().save(commit=False)   
		print("update")
		if commit:
			user.save() 
		return user
 
