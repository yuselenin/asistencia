from django.contrib.auth.models import AbstractUser
from django.db import models


class Persona(models.Model):
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    dnicodigo = models.PositiveIntegerField()
    email = models.EmailField()
    numerocelular = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)


class Usuario(AbstractUser):
    persona = models.OneToOneField(Persona, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
