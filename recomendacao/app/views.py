from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'TelaLogin.html')

def cadastro(request):
    return render(request, 'CadastroUsuario.html')

def cadrm(request):
    return render(request, 'CadastroRM.html')

def principal(request):
    return render(request, 'TelaPrincipal.html')

def TelaPrincipal(request):
    return render(request, 'TelaPrincipal.html')