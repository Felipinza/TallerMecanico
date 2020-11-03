from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name='ID Categoria')
    nombreCategoria=models.CharField(max_length=100, verbose_name='Nombre Categoria')

    def __str__(self):
        return self.nombreCategoria

class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name='ID Imagen')
    texto = models.CharField(max_length=120, verbose_name='Texto Descriptivo')
    nombre = models.CharField(max_length=50, verbose_name='Nombre Imagen')
    fechaRegistro = models.DateTimeField(verbose_name='Fecha Hora Registro')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Usuario(models.Model):
    email=models.EmailField(max_length=70, primary_key=True, verbose_name='Email')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    #apellidos=models.CharField(max_length=70, verbose_name='Apellidos')
    #nickname=models.CharField(max_length=20, verbose_name='Nickname')
    #password=models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.email

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

    def __str__(self):
        return self.patente

class Servicio(models.Model):
    idServicio=models.AutoField(primary_key=True, verbose_name='ID Servicio')
    nombre=models.CharField(max_length=40, verbose_name='Marca')
    descripcion=models.CharField(max_length=100, verbose_name='Descripcion')
    disponible=models.BooleanField(verbose_name='Disponibilidad')

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