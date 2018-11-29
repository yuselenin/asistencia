from django.contrib import admin

from .models.asistencia import Asistencia
from .models.evento import Evento
from .models.evento_programado import EventoProgramado
from .models.matricula import Matricula
from .models.mensaje import Mensaje
from .models.periodo import Periodo
from .models.plan_mensaje import PlanMensaje

# Register your models here.
admin.site.register(Asistencia)
admin.site.register(EventoProgramado)
admin.site.register(Evento)
admin.site.register(Matricula)
admin.site.register(Mensaje)
admin.site.register(Periodo)
admin.site.register(PlanMensaje)
