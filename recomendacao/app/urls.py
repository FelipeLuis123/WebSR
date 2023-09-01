from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from rest_framework import routers
from . import views
from .viewsets import AutorFormSets
from .viewsets import CadastroRMViewSets

router = routers.DefaultRouter()
router.register(r'cadastrorm', CadastroRMViewSets, basename="Cadastrar Recomendação")


router = routers.DefaultRouter()
router.register(r'autor', AutorFormSets, basename="Autor")

urlpatterns = [
    path('', views.login, name='login'),
    path('recomendacao/login', views.login, name='login'),
    path('recomendacao/cadastro', views.cadastro, name='cadastro'),
    path('recomendacao/principal', views.principal, name='principal'),
    path('recomendacao/cadrm', views.cadrm, name='cadrm'),
    path('recomendacao/autor/add', views.autor_add, name='autor_add'),
    path('recomendacao/autor/', views.autor, name='autor'),
    path('recomendacao/autor/edit/<int:autor_pk>/', views.autor_edit, name='autor_edit'),
    path('recomendacao/autor/delete/<int:autor_pk>', views.autor_delete, name='autor_delete'),
    path('recomendacao/ajuste-fonte/', views.ajuste_fonte, name='ajuste_fonte'),





]
