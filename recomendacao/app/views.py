from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'TelaLogin.html')

def cadastro(request):
    return render(request, 'CadastroUsuario.html')

def cadastroRM(request):
    return render(request, 'CadastroRM.html')