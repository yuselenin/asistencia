from rest_framework import viewsets

from ..models.evento import Evento
from ..serializers.evento import EventoSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
