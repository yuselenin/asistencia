from rest_framework import viewsets

from ..models.periodo import Periodo
from ..serializers.periodo import PeriodoSerializer


class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer
