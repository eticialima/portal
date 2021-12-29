from django.shortcuts import render, redirect
from django.urls import reverse_lazy 
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
from perfil.forms import ProfileForm
from perfil.models import Profile   

from accounts.models import CustomUser
from perfil.models import Profile
  
class ProfileView(DetailView):
    model = CustomUser
    template_name = "profile/profile.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    context_object_name = "perfil"
    object = None

    def get_object(self, queryset=None):
        return self.model.objects.select_related('profile').prefetch_related("posts").get(user_name=self.kwargs.get(self.slug_url_kwarg)) 

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
 

class ProfileEditView(UpdateView):
    model = Profile
    template_name = "profile/edit-profile.html"
    context_object_name = "profile"
    object = None
    fields = "__all__"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def post(self, request, *args, **kwargs):
        print(request.POST.get('first_name'))
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name') 
        user.save()
        profile = user.profile
        profile.about = request.POST.get('about')
        profile.occupation = request.POST.get('occupation')
        profile.description = request.POST.get('description') 
        if request.POST.get('gender') == "Homem":
            profile.gender = "Homem"
        else:
            profile.gender = "Mulher"
        profile.country = request.POST.get('country')
        profile.city = request.POST.get('city')
        profile.phone = request.POST.get('phone')
        profile.save()
        messages.success(self.request, 'Alterações salva com sucesso!!!')
        return redirect(reverse_lazy('profile:edit-profile')) 