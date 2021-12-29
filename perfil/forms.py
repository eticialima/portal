from django import forms 
from perfil.models import Network, Profile    

class NetworkForm(forms.ModelForm):
    class Meta:
        model = Network
        fields = '__all__' 
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__' 

