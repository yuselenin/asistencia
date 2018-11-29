from rest_framework import serializers

from ..models.asistencia import Asistencia


# Serializers define the API representation.
class AsistenciaSerializer(serializers.ModelSerializer):
    codigo = serializers.SerializerMethodField()

    class Meta:
        model = Asistencia
        fields = "__all__"

    def get_codigo(self, obj):
        return obj.matricula.persona.dni
