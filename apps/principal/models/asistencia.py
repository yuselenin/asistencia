from django.db import models

from apps.utilitarios.models import Usuario
from .evento_programado import EventoProgramado
from .matricula import Matricula


class Asistencia(models.Model):
    fecha_hora = models.DateTimeField(auto_now=True)
    ofline = models.BooleanField(default=False, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    evento_programado = models.ForeignKey(EventoProgramado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return "%s -> %s:%s" % (self.fecha_hora, self.matricula, self.evento_programado)
