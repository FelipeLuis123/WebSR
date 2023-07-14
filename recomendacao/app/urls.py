from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('', views.login, name = 'login'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('principal', views.principal, name='principal'),
    path('cadrm', views.cadrm, name='cadrm'),

]
