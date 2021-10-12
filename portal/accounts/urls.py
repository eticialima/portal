from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth.views import PasswordResetDoneView
from accounts.views import ( UserLogin,	UserCreate,	UserChange,	PasswordChange,
	PasswordReset, PasswordResetConfirm, PasswordResetComplete, UserDelete,
	UserListView, TimeOutView)

urlpatterns = [
	path('login/', UserLogin.as_view(), name='login'),
	path('user-new/', UserCreate.as_view(), name='user-new'),
	path('usuarios/', UserListView.as_view(), name='users'),
	path('<int:pk>/update/', UserChange.as_view(), name='user-change'),
	path('password-change/', PasswordChange.as_view(), name='password-change'),
	path('password-reset/', PasswordReset.as_view(), name='password-reset'),
	path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name="password_reset_confirm"),
	path('reset/done/', PasswordResetComplete.as_view(), name='password_reset_complete'),
	path('<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
	path('', include('django.contrib.auth.urls')), 
	path('timeout/', TimeOutView.as_view(), name='timeout'), 
 
]