from django.db import models

from .evento import Evento


class EventoProgramado(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Evento programado"
        verbose_name_plural = "Eventos programados"

    def __str__(self):
        return "%s %s" % (self.fecha, self.evento)
