from rest_framework import serializers

from ..models import Persona


# Serializers define the API representation.
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"
