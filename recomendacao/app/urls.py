from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from rest_framework import routers
from . import views
from .viewsets import AutorFormSets



router = routers.DefaultRouter()
router.register(r'autor', AutorFormSets, basename="Autor")

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('principal', views.principal, name='principal'),
    path('cadrm', views.cadrm, name='cadrm'),
    path('autor/add', views.autor_add, name='autor_add'),
    path('autor/', views.autor, name='autor'),
    path('recomendacao/autor/edit/<int:autor_pk>/', views.autor_edit, name='autor_edit'),
    path('autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),




]
