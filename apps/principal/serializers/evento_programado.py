from rest_framework import serializers

from ..models.evento_programado import EventoProgramado


# Serializers define the API representation.
class EventoProgramadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoProgramado
        fields = "__all__"
