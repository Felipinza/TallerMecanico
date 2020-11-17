"""Prueba1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prueba import views as views_principal
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views_principal.IndexTemplate),
    path('mecanico1/', views_principal.Mecanico1),
    path('mecanico2/', views_principal.Mecanico2),
    path('mecanico3/', views_principal.Mecanico3),
    path('mecanico4/', views_principal.Mecanico4),
    path('mecanico5/', views_principal.Mecanico5),
    path('inventario/', views_principal.Inventario),
    path('servicios/', views_principal.Servicios),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views_principal.Registro),
    path('RegistrarUsuario/', views_principal.RegistrarUsuario),
    path('registroauto/', views_principal.Vehiculo),
    path('RegistrarVehiculo/', views_principal.RegistrarVehiculo),
    path('BorrarVehiculo/<patente>', views_principal.BorrarVehiculo),
    path('subirimagen/', views_principal.SubirImagen),
    path('GuardarImagen/', views_principal.GuardarImagen),
    path('BorrarImagen/<int:idImagen>', views_principal.BorrarImagen),
    path('galeria/', views_principal.Galeria),
    path('borrarimagen/', views_principal.EliminarImagen),
    path('taller/', views_principal.Taller),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)