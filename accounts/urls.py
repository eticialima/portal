from django.urls import path, include 
from django.contrib.auth.views import PasswordResetDoneView
from accounts import views

app_name = "accounts"
urlpatterns = [
	path('login/', views.UserLogin.as_view(), name='login'),

	path('user-new/', views.UserCreate.as_view(), name='user-new'), 

	path('<int:pk>/update/', views.UserChange.as_view(), name='user-change'), 

	path('password-change/', views.PasswordChange.as_view(), name='password-change'),
	
	path('password-reset/', views.PasswordReset.as_view(), name='password-reset'),

	path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),

	path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name="password_reset_confirm"),
	
	path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),
	
	path('<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
	
	path('', include('django.contrib.auth.urls')),
	
	path('timeout/', views.TimeOutView.as_view(), name='timeout'),
]