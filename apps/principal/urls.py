from django.conf.urls import url, include
from rest_framework import routers

from .viewsets.asistencia import AsistenciaViewSet
from .viewsets.evento import EventoViewSet
from .viewsets.evento_programado import EventoProgramadoViewSet
from .viewsets.matricula import MatriculaViewSet
from .viewsets.mensaje import MensajeViewSet
from .viewsets.periodo import PeriodoViewSet
from .viewsets.plan_mensaje import PlanMensajeViewSet

router = routers.DefaultRouter()
router.register(r'asistencia', AsistenciaViewSet)
router.register(r'evento_programado', EventoProgramadoViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'matricula', MatriculaViewSet)
router.register(r'mensaje', MensajeViewSet)
router.register(r'periodo', PeriodoViewSet)
router.register(r'plan_mensaje', PlanMensajeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
