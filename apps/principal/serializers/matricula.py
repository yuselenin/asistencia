from rest_framework import serializers

from ..models.matricula import Matricula


# Serializers define the API representation.
class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"
