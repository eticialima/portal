from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from accounts.forms import CustomUserCreateForm, CustomUserChangeForm
from accounts.models import CustomUser
 
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreateForm
	form = CustomUserChangeForm
	model = CustomUser 

	list_display = ('user_name','email','first_name','last_name','type_user','is_staff')
	readonly_fields = ['date_joined'] 
	
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal information', 
		{'fields': ('user_name','first_name', 'last_name','type_user')}),
		('Permissions', 
		{'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)