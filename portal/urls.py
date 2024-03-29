"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from perfil.views import NetworkViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register(r'users', ProfileViewSet)
router.register(r'net', NetworkViewSet)

urlpatterns = [ 
    path('api/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 

    path('admin/', admin.site.urls),

    path('accounts/', include('accounts.urls')), 

    path('', include('home.urls')),   

    path('painel/', include('painel.urls')),

    path('perfil/', include('perfil.urls')),

    path('post/', include('post.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)