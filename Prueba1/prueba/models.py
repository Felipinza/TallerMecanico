from django.db import models
from django.conf import settings

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria=models.CharField(max_length=100, verbose_name='Nombre Categoria')

    def __str__(self):
        return str(self.idCategoria)

class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name='ID Imagen')
    texto = models.CharField(max_length=120, verbose_name='Texto Descriptivo')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Imagen')
    fechaRegistro = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Hora Registro')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    mecanico=models.CharField(max_length=80, default="mecanico", verbose_name='Nombre Mecanico')
    archivo = models.ImageField(upload_to="img_subidas", null=True)

    def __str__(self):
        return str(self.idImagen)

class Vehiculo(models.Model):
    patente=models.CharField(max_length=6, verbose_name='Patente')
    marca=models.CharField(max_length=40, verbose_name='Marca')
    modelo=models.CharField(max_length=50, verbose_name='Modelo')
    ano=models.IntegerField(verbose_name='Ano')
    litros=models.CharField(max_length=20, verbose_name='Litros')
    configuracion=models.CharField(max_length=30, verbose_name='Configuracion')
    kilometraje=models.IntegerField(verbose_name='Kilometraje')
    transmision=models.CharField(max_length=20, verbose_name='Transmision')
    color=models.CharField(max_length=20, verbose_name='Color')
    cliente=models.CharField(max_length=80, verbose_name='Nombre Cliente')

    def __str__(self):
        return self.patente

class Servicio(models.Model):
    idServicio=models.AutoField(primary_key=True, verbose_name='ID Servicio')
    nombre=models.CharField(max_length=40, verbose_name='Marca')
    descripcion=models.CharField(max_length=100, verbose_name='Descripcion')
    disponible=models.BooleanField(verbose_name='Disponibilidad')
    precio=models.IntegerField(verbose_name='Precio')

    def __str__(self):
        return self.idServicio

class Mecanico(models.Model):
    rut=models.CharField(max_length=9, verbose_name='Rut Mecanico')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    apellido1=models.CharField(max_length=20, verbose_name='Apellido Paterno')
    apellido2=models.CharField(max_length=20, verbose_name='Apellido Materno')
    especialidad=models.CharField(max_length=9, verbose_name='Especialidad')
    fecha_contrato=models.DateField(verbose_name='Fecha Contrato')

    def __str__(self):
        return self.rut
