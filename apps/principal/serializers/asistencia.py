from rest_framework import serializers

from ..models.asistencia import Asistencia


# Serializers define the API representation.
class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = "__all__"
