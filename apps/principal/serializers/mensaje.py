from rest_framework import serializers

from ..models.mensaje import Mensaje


# Serializers define the API representation.
class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = "__all__"
