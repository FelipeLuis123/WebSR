from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('cadastroRM', views.cadastroRM, name='cadastroRM'),
]
