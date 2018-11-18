from django.contrib import admin

from .models.asistencia import Asistencia
from .models.evento import Evento
from .models.evento_programado import EventoProgramado
from .models.matricula import Matricula
from .models.mensaje import Mensaje
from .models.periodo import Periodo
from .models.plan_mensaje import PlanMensaje

# Register your models here.
admin.register(Asistencia)
admin.register(EventoProgramado)
admin.register(Evento)
admin.register(Matricula)
admin.register(Mensaje)
admin.register(Periodo)
admin.register(PlanMensaje)
