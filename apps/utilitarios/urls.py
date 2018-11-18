from django.conf.urls import url, include
from rest_framework import routers

from .viewsets.persona import PersonaViewSet
from .viewsets.usuario import UsuarioViewSet

router = routers.DefaultRouter()
router.register(r'persona', PersonaViewSet)
router.register(r'usuario', UsuarioViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
