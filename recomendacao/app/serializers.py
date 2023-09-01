from .models import Autor, CadastroRM
from rest_framework import serializers


class CadastroRMSerializers(serializers.ModelSerializer):
    class Meta:
        model = CadastroRM
        fields = '__all__'



class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['Nome', 'Email', 'Curso', 'Telefone', 'Matricula', 'Curso']
