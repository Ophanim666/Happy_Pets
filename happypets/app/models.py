from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    fecha_duracion = models.DateField()

    def __str__(self):
        return self.nombre, self.precio, self.descripcion, self.fecha_duracion

    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre, self.apellido, self.correo, self.telefono


class Mascota(models.Model):
    especie = models.CharField(max_length = 50)
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    fecha_rescate = models.DateField()

    def __str__(self):
        return self.especie, self.nombre, self.descripcion, self.fecha_rescate
