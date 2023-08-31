from django.db import models


# Create your models here.

class Autor(models.Model):
    Nome = models.CharField(max_length=255)
    Email = models.EmailField(null=True, blank=True)
    Curso = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50, )
    Cpf = models.CharField(max_length=11, )
    Matricula = models.CharField(max_length=50 )
    Senha = models.CharField(max_length=50  )
    Confirmar_Senha = models.CharField(max_length=50 )
