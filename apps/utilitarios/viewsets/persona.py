from rest_framework import viewsets

from ..models import Persona
from ..serializers.persona import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
