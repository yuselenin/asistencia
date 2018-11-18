from rest_framework import serializers

from ..models.periodo import Periodo


# Serializers define the API representation.
class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = "__all__"
