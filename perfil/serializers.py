from perfil.models import Profile, Network
from rest_framework import serializers
 
class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['id','user','name','url']

class ProfileSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'occupation', 'description', 'gender', 'phone', 'city', 'country']

