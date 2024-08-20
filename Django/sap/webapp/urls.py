from django.urls import path
from .views import bienvenido
from personas.views import DomicilioVieSet ,PersonasVistaSet 
from rest_framework.routers import DefaultRouter



router =DefaultRouter()
router.register('personas/',PersonasVistaSet,basename='personas')
router.register('domicilio/',DomicilioVieSet,basename='domicilio')


urlpatterns =router.urls
