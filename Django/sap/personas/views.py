from django.forms import modelform_factory
from django.shortcuts import get_object_or_404 , render
from rest_framework import serializers
from .models import Persona ,Domicilo
from rest_framework.generics import ListAPIView ,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets





# Create your views here.
class PersonaSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields= ('__all__')
class DomicilioSeralizer(serializers.ModelSerializer):
    class Meta:
        model=Domicilo
        fields= ('__all__')


class PersonasVistaSet(viewsets.ModelViewSet):
    queryset= Persona.objects.all()
    serializer_class=PersonaSeralizer

class DomicilioVieSet(viewsets.ModelViewSet):
    queryset= Domicilo.objects.all()
    serializer_class=DomicilioSeralizer
# class ApliLIsarPersonas(ListAPIView):
#     serializer_class=PersonaSeralizer
#     queryset=Persona.objects.all()


# class PerosnaDetalle(ListAPIView):
#     def get(self,request,persona_id):
#       persona= get_object_or_404(Persona,id=persona_id)
#       serializer_class=PersonaSeralizer(persona)
      
#       return Response(serializer_class.data)

#una fomra

#############################################
# class PersonaLista(ListCreateAPIView):
#     queryset=Persona.objects.all()
#     serializer_class= PersonaSeralizer


# class Detalleperosna(RetrieveUpdateDestroyAPIView):
     
#     queryset= Persona.objects.all()
#     serializer_class=PersonaSeralizer
       