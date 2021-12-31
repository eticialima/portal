from django.http import HttpResponseRedirect 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.base import View  
from perfil.models import Profile  

class ProfileAddLike(LoginRequiredMixin,View):
    slug_field = "username"
    slug_url_kwarg = "username"
    def post(self, request, pk, *args, **kwargs):
        profile = Profile.objects.get(pk=pk) 
        is_like = False
        for like in profile.likes.all():
            if like == request.user:
                is_like = True
                break 
        if not is_like:
            profile.likes.add(request.user)

        if is_like:
            profile.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)