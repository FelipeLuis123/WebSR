"""
URL configuration for recomendacao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from app import viewsets as cadastroRMViewSets

# from recomendacao.app.viewsets import CadastroRMViewSets

route = routers.DefaultRouter()

route.register(r' app', cadastroRMViewSets.CadastroRMViewSets, basename="CadastroRMV")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app/', include(route.urls)),


]
