from rest_framework import viewsets

from ..models.plan_mensaje import PlanMensaje
from ..serializers.plan_mensaje import PlanMensajeSerializer


class PlanMensajeViewSet(viewsets.ModelViewSet):
    queryset = PlanMensaje.objects.all()
    serializer_class = PlanMensajeSerializer
