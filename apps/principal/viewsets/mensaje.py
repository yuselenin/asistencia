from rest_framework import viewsets

from ..models.mensaje import Mensaje
from ..serializers.mensaje import MensajeSerializer


class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
