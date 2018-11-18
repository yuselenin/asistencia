from rest_framework import serializers

from ..models.evento import Evento


# Serializers define the API representation.
class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"
