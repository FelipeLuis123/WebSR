from rest_framework import viewsets
from .serializers import AutorSerializer, CadastroRMSerializers
from .models import Autor, CadastroRM


class CadastroRMViewSets(viewsets.ModelViewSet):
    model = CadastroRM
    serializer_class = CadastroRMSerializers
    queryset = CadastroRM.objects.all()


class AutorFormSets(viewsets.ModelViewSet):
    model = Autor
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    exclude = ()
