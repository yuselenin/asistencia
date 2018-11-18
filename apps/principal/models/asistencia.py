from django.db import models

from apps.utilitarios.models import Usuario
from .evento_programado import EventoProgramado
from .matricula import Matricula


class Asistencia(models.Model):
    codigo = models.CharField(max_length=10)
    nombres = models.CharField(max_length=30)
    fecha_hora = models.DateTimeField()
    ofline = models.CharField(max_length=10)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE)
    evento_programado = models.ForeignKey(EventoProgramado, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    def __str__(self):
        return "%s -> %s:%s" % (self.codigo, self.matricula, self.evento_programado)
