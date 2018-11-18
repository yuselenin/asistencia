from django.db import models


class Mensaje(models.Model):
    numero_envio = models.CharField(max_length=10)
    numero_recepcion = models.CharField(max_length=10)
    mensaje_entregado = models.CharField(max_length=60)
    tipo_mensaje = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"

    def __str__(self):
        return "%s -> %s: %s" % (self.numero_envio, self.numero_recepcion, self.mensaje_entregado)
