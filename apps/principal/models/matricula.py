from django.db import models

from apps.utilitarios.models import Persona
from .periodo import Periodo


class Matricula(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    cantidad_horas = models.IntegerField()

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return "%s, %s" % (self.persona, self.periodo)
