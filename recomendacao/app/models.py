from django.db import models
from django.db import models
from uuid import uuid4

class CadastroRM(models.Model):
    nome = models.CharField(max_length=255, )
    telefone = models.IntegerField()
    id_RM = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo_imovel = models.CharField(max_length=255)
    logradouro = models.CharField(max_length=255)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.IntegerField()
    valor_aluguel = models.IntegerField()
    quantidade_quartos = models.IntegerField()
    quantidade_banheiros = models.IntegerField()  # Use IntegerField for quantity fields
    area_total_imovel = models.IntegerField()
    descricao = models.CharField(max_length=255)  # "Descricao" should be lowercase "descricao"
    foto_imovel = models.ImageField(upload_to='imagens/', blank=True, null=True)

class Autor(models.Model):
    Nome = models.CharField(max_length=255)
    Email = models.EmailField(null=True, blank=True)
    Curso = models.CharField(max_length=50)
    Telefone = models.CharField(max_length=50, )
    Cpf = models.CharField(max_length=11, )
    Matricula = models.CharField(max_length=50 )
    Senha = models.CharField(max_length=50  )
    Confirmar_Senha = models.CharField(max_length=50 )
