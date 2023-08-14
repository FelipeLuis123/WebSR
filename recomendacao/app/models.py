from django.db import models

# Create your models here.


class Clientes(models.Model):
    nome = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)