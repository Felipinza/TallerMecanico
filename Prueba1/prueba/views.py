from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render
from prueba import models

def IndexTemplate(request):
    return render(request, 'index.html')

def Galeria(request):
    return render(request, 'galeria.html')
    
def Registro(request):
    return render(request, 'registro.html')



def RegistrarVehiculo(request):
    if request.method=='POST':
        cliente=request.POST.get('cliente')
        patente=request.POST.get('patente')
        marca=request.POST.get('marca')
        modelo=request.POST.get('modelo')
        ano=request.POST.get('ano')
        litros=request.POST.get('litros')
        configuracion=request.POST.get('configuracion')
        kilometraje=request.POST.get('kilometraje')
        transmision=request.POST.get('transmision')
        color=request.POST.get('color')

        auxVehiculo=models.Vehiculo()
        auxVehiculo.patente=patente
        auxVehiculo.marca=marca
        auxVehiculo.modelo=modelo
        auxVehiculo.ano=ano
        auxVehiculo.litros=litros
        auxVehiculo.configuracion=configuracion
        auxVehiculo.kilometraje=kilometraje
        auxVehiculo.transmision=transmision
        auxVehiculo.color=color
        auxVehiculo.cliente=cliente
        auxVehiculo.save()

    return HttpResponseRedirect("/index/")
