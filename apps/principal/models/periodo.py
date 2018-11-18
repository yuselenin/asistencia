from django.db import models


class Periodo(models.Model):
    periodo = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return "%s" % (self.periodo)
