from rest_framework import viewsets

from ..models.evento_programado import EventoProgramado
from ..serializers.evento_programado import EventoProgramadoSerializer


class EventoProgramadoViewSet(viewsets.ModelViewSet):
    queryset = EventoProgramado.objects.all()
    serializer_class = EventoProgramadoSerializer
