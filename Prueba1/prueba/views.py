from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from prueba import models

def IndexTemplate(request):
    return render(request, 'index.html')

def Galeria(request):
    return render(request, 'galeria.html')

def Login(request):
    return render(request, 'login.html')

def Registro(request):
    return render(request, 'registro.html')



def RegistrarUsuario(request):
    if request.method=='POST':
        nombre=request.POST.get('name')
        correo=request.POST.get('correo')

        auxUsuario=models.Usuario()
        auxUsuario.nombre=nombre
        auxUsuario.email=correo
        auxUsuario.save()

    return HttpResponseRedirect("/index/")
