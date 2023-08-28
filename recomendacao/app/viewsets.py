from rest_framework import viewsets
from .serializers import AutorSerializer
from .models import Autor


class AutorFormSets(viewsets.ModelViewSet):
    model = Autor
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    exclude = ()
