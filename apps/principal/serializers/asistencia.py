from rest_framework import serializers

from ..models.asistencia import Asistencia


# Serializers define the API representation.
class AsistenciaSerializer(serializers.ModelSerializer):
    codigo = serializers.SerializerMethodField()
    nombres = serializers.SerializerMethodField()
    celular = serializers.SerializerMethodField()

    class Meta:
        model = Asistencia
        fields = "__all__"

    def get_codigo(self, obj):
        return obj.matricula.persona.dni

    def get_nombres(self, obj):
        return "%s %s" % (obj.matricula.persona.nombres, obj.matricula.persona.apellidos)

    def get_celular(self, obj):
        return obj.matricula.persona.numerocelular
