from django.db import models


class PlanMensaje(models.Model):
    tipo_mensaje = models.CharField(max_length=10)
    mensaje_previo = models.CharField(max_length=60)

    class Meta:
        verbose_name = "Plan mensaje"
        verbose_name_plural = "Plan mensaje"

    def __str__(self):
        return "%s" % (self.tipo_mensaje)
