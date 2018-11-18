from rest_framework import viewsets

from ..models.matricula import Matricula
from ..serializers.matricula import MatriculaSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
