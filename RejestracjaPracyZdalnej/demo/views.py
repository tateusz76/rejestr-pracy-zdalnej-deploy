from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class PracownikList(generics.ListCreateAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-list'


class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownik-details'

class FirmaList(generics.ListCreateAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer
    name = 'firma-list'


class FirmaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Firma.objects.all()
    serializer_class = FirmaSerializer
    name = 'firma-details'

class PracaList(generics.ListCreateAPIView):
    queryset = Praca.objects.all()
    serializer_class = PracaSerializer
    name = 'praca-list'


class PracaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Praca.objects.all()
    serializer_class = PracaSerializer
    name = 'praca-details'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'pracownicy': reverse(PracownikList.name, request=request),
                         'firmy': reverse(FirmaList.name, request=request),
                         'prace': reverse(PracaList.name, request=request),})
