from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from .forms import AutorForm
from .models import Autor

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Verifique as credenciais do usuário
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Credenciais corretas, faça o login
            login(request, user)
            return redirect('principal')  # Redirecione para a página principal após o login
        else:
            # Credenciais incorretas, exiba uma mensagem de erro na página de login
            error_message = "Credenciais inválidas. Por favor, verifique seu email e senha."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'TelaLogin.html')

def Tlogin(request):
    return render( redirect, 'TelaLogin.html')

def cadastro(request):
    return render(request, 'CadastroUsuario.html')


def cadrm(request):
    return render(request, 'CadastroRM.html')


def principal(request):
    return render(request, 'TelaPrincipal.html')


def TelaPrincipal(request):
    return render(request, 'TelaPrincipal.html')


def autor(request):
    autores = Autor.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'autor.html', context)



def autor_add(request):
    form =AutorForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('principal' )

    context ={
        'form': form
    }
    return render(request,'autor_add.html', context)


def autor_edit(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('autor')  # Redirecionar para a lista de autores após salvar
    context = {
        'form': form,
        'autor': autor,  # Passar o objeto autor para a template
    }
    return render(request, 'autor_edit.html', context)


def autor_delete(request, autor_pk):
    autor = Autor.objects.get(pk=autor_pk)
    autor.delete()

    return redirect('autor')
from django.shortcuts import render

def ajuste_fonte(request):
    return render(request, 'font_size_adjust.html')


