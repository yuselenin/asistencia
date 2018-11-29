import sys

import qrcode
from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from six import BytesIO


class Persona(models.Model):
    nombres = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    dni = models.PositiveIntegerField()
    email = models.EmailField()
    numerocelular = models.PositiveIntegerField()
    qrcode = models.ImageField(upload_to='qrcode', blank=True, null=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return "%s %s" % (self.nombres, self.apellidos)


@receiver(post_save, sender=Persona, dispatch_uid="generate_qrcode")
def generate_qrcode(sender, created, instance, **kwargs):
    if created or not instance.qrcode:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=3,
        )
        qr.add_data(instance.dni)
        qr.make(fit=True)
        img = qr.make_image()
        filename = 'u-%s.png' % (instance.dni)
        # img.save(""filename)
        buffer = BytesIO()
        img.save(buffer)  # , format='JPEG', quality=100)
        buffer.seek(0)
        filebuffer = InMemoryUploadedFile(
            buffer,
            'ImageField',
            filename,
            'image/png',  # 'image/jpeg',
            sys.getsizeof(buffer),
            None
        )
        post_save.disconnect(generate_qrcode, sender=Persona)
        instance.qrcode.save(filename, filebuffer)
        post_save.connect(generate_qrcode, sender=Persona)


class Usuario(AbstractUser):
    persona = models.OneToOneField(
        Persona, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username
