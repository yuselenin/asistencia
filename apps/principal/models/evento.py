from django.db import models

from .periodo import Periodo


class Evento(models.Model):
    nombre = models.CharField(max_length=40)
    lugar = models.CharField(max_length=40)
    tiempo_tolerancia = models.CharField(max_length=6)
    estado = models.CharField(max_length=5)
    longitud = models.IntegerField()
    latitud = models.IntegerField()
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return "%s" % (self.nombre)
