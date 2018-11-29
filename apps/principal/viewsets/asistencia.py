from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.principal.models.evento import Evento
from apps.utilitarios.models import Persona
from ..models.asistencia import Asistencia
from ..serializers.asistencia import AsistenciaSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

    def create(self, request, *args, **kwargs):
        # este codigo es provisional

        persona = Persona.objects.filter(dni=request.data.get('codigo', None))
        if persona.exists():
            if persona[0].matricula_set.all():
                request.data['usuario'] = request.user.id
                request.data['matricula'] = persona[0].matricula_set.all()[0].id
                request.data['evento_programado'] = Evento.objects.first().id
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response(data="No está matriculado la persona", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data="No se encontró a la persona", status=status.HTTP_400_BAD_REQUEST)
