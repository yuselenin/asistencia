from rest_framework import serializers

from ..models.plan_mensaje import PlanMensaje


# Serializers define the API representation.
class PlanMensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMensaje
        fields = "__all__"
