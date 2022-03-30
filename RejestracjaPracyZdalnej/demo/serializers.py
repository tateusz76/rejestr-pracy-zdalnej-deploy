from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class PracownikSerializer(serializers.HyperlinkedModelSerializer):
    firma = serializers.SlugRelatedField(queryset=Firma.objects.all(), slug_field='nazwaFirmy')

    class Meta:
        model = Pracownik
        fields = ['id', 'imie', 'nazwisko', 'pesel', 'firma', 'czyKierownik', 'czyAdministrator', 'login', 'mail',
                  'haslo']


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'is_staff', 'is_superuser', 'username', 'password', 'first_name', 'last_name', 'pesel',
                  'phone', 'firma']


class FirmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Firma
        fields = ['id', 'nazwaFirmy']


class ZapisPracySerializer(serializers.ModelSerializer):
    class Meta:
        model = ZapisPracy
        fields = ['id', 'idPracownika', 'data', 'przepracowaneMinuty']


class PracaSerializer(serializers.ModelSerializer):
    # idPracownika = serializers.SlugRelatedField(queryset=Pracownik.objects.all(), slug_field='idPracownika')
    class Meta:
        model = Praca
        fields = ['idPracownika', 'dataRozpoczecia', 'dataZakonczenia', 'minutyStart', 'minutyPozostalo', 'zlecajacy']
