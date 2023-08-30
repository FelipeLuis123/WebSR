from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o  seu nome'}),
            'Curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu curso'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu email'}),
            'Telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu telefone'}),
            'Cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o seu CPF'}),
            'Matricula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o numero da sua matrícula'}),
             'Senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a sua Senha'}),
            'Confirmar_Senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a sua Senha novamente'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('Senha')
        confirmar_senha = cleaned_data.get('Confirmar_Senha')

        if senha and confirmar_senha and senha != confirmar_senha:
            self.add_error('Nome', 'As senhas não coincidem.')

        if len(senha) < 8:
            self.add_error('Nome', 'A senha deve ter pelo menos 8 caracteres.')

        return cleaned_data

