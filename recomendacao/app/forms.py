from django.forms import ModelForm
from django import forms
from .models import Clientes

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes
        fields = ['nome', 'cpf']
