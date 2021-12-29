from django.urls import path
from perfil.views import ProfileView, ProfileEditView

app_name = "profile"
urlpatterns = [
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('<slug:username>', ProfileView.as_view(), name="user-profile"),
]
 