from django.urls import path, include
from . import views
from django.contrib import admin

admin.site.site_url = 'http://127.0.0.1:8000/demo/'
urlpatterns = [
    path('pracownik', views.PracownikList.as_view(), name='pracownik-list'),
    path('pracownik/<int:pk>', views.PracownikDetail.as_view(), name='pracownik-details'),
    path('firma', views.FirmaList.as_view(), name='firma-list'),
    path('firma/<int:pk>', views.FirmaDetail.as_view(), name='firma-details'),
    path('praca', views.PracaList.as_view(), name='praca-list'),
    path('praca/<int:pk>', views.PracaDetail.as_view(), name='praca-details'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]