from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
import mysql.connector
from mysql.connector import Error
from prueba import models
from django.contrib.auth.models import User

# RENDER INICIO
def IndexTemplate(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    nombre_pagina = "inicio"
    return render(request, 'index.html', {'nombre_pagina':nombre_pagina,'es_mecanico':es_mecanico})


# RENDER MECANICOS
def Mecanico1(request):
    nombre_pagina = "mecanicos"
    return render(request, 'mecanico1.html',{'nombre_pagina':nombre_pagina})

def Mecanico2(request):
    nombre_pagina = "mecanicos"
    return render(request, 'mecanico2.html',{'nombre_pagina':nombre_pagina})

def Mecanico3(request):
    nombre_pagina = "mecanicos"
    return render(request, 'mecanico3.html',{'nombre_pagina':nombre_pagina})

def Mecanico4(request):
    nombre_pagina = "mecanicos"
    return render(request, 'mecanico4.html',{'nombre_pagina':nombre_pagina})

def Mecanico5(request):
    nombre_pagina = "mecanicos"
    return render(request, 'mecanico5.html',{'nombre_pagina':nombre_pagina})


# RENDER INVENTARIO
def Inventario(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    nombre_pagina = "inventario"
    return render(request, 'inventario.html', {'nombre_pagina':nombre_pagina,'es_mecanico':es_mecanico})

# RENDER SERVICIOS
def Servicios(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    nombre_pagina = "servicios"
    return render(request, 'servicios.html', {'nombre_pagina':nombre_pagina,'es_mecanico':es_mecanico})

# RENDER GALERIA
def Galeria(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    imagenes = models.Imagen.objects.all()
    nombre_pagina = "galeria"
    return render(request, 'galeria.html', {'imagenes':imagenes,'nombre_pagina':nombre_pagina,'es_mecanico':es_mecanico})


# RENDER TALLER
def Taller(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    nombre_pagina = "taller"
    return render(request, 'taller.html', {'nombre_pagina':nombre_pagina, 'es_mecanico':es_mecanico})


# RENDER REGISTRO USUARIO
def Registro(request):
    nombre_pagina = "registro"
    return render(request, 'registro.html',{'nombre_pagina':nombre_pagina})


# RENDER REGISTRAR VEHICULO
def RegistroAuto(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    return render(request, 'registroauto.html', {'es_mecanico':es_mecanico})


# RENDER PAGINA SUBIR IMAGEN
def SubirImagen(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    resultados = models.Categoria.objects.all()
    return render(request, "subirimagen.html", {"categorias": resultados, 'es_mecanico':es_mecanico})


# RENDER PAGINA ELIMINAR IMAGEN
def EliminarImagen(request):
    es_mecanico = request.user.groups.filter(name='mecanico').exists()
    categorias = models.Categoria.objects.all()

    imagenes = models.Imagen.objects.all()

    if request.POST.get('categoria'):
        categoria = request.POST.get('categoria')
        imagenes = models.Imagen.objects.filter(categoria=categoria)

    return render(request, 'borrarimagen.html', {'imagenes':imagenes, 'es_mecanico':es_mecanico, 'categorias':categorias})

# PERMANENCIA MANTENEDOR VEHICULO
def RegistrarVehiculo(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        patente = request.POST.get('patente')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        litros = request.POST.get('litros')
        configuracion = request.POST.get('configuracion')
        kilometraje = request.POST.get('kilometraje')
        transmision = request.POST.get('transmision')
        color = request.POST.get('color')

        auxVehiculo = models.Vehiculo()
        auxVehiculo.patente = patente
        auxVehiculo.marca = marca
        auxVehiculo.modelo = modelo
        auxVehiculo.ano = ano
        auxVehiculo.litros = litros
        auxVehiculo.configuracion = configuracion
        auxVehiculo.kilometraje = kilometraje
        auxVehiculo.transmision = transmision
        auxVehiculo.color = color
        auxVehiculo.cliente = cliente
        auxVehiculo.save()

    return HttpResponseRedirect("/index/")

# PERMANENCIA MANTENEDOR IMAGENES
def GuardarImagen(request):
    if request.method == 'POST':
        mecanico = request.POST.get('mecanico')
        texto = request.POST.get('texto')
        nombre = request.POST.get('nombre')
        archivo = request.FILES.get('archivo')
        categoria = request.POST.get('categoria')

        c = models.Categoria.objects.get(idCategoria=categoria)

        auxImagen = models.Imagen(
            mecanico=mecanico, texto=texto, nombre=nombre, archivo=archivo, categoria=c)

        auxImagen.save()

        return HttpResponseRedirect("/index/")
    else:
        return HttpResponseRedirect("/subirimagen/")

def BorrarImagen(request, idImagen):
    imagen = models.Imagen.objects.get(idImagen=idImagen)
    imagen.delete()

    return HttpResponseRedirect('/galeria/')


def RegistrarUsuario(request):
        if request.method=='POST':
            username=request.POST.get('username')
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            email=request.POST.get('email')
            password=request.POST.get('password')

            auxUsuario=User()

            auxUsuario.username=username
            auxUsuario.first_name=first_name
            auxUsuario.last_name=last_name
            auxUsuario.email=email

            auxUsuario.set_password(password)
            auxUsuario.save()
        
        return HttpResponseRedirect("/index/")
