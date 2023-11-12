from django.db import models

# Create your models here.
#modelo del Alumno

class Alumno(models.Model):
    DNI = models.IntegerField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField( blank=True, null=True, default='No asignado')
    telefono= models.CharField(max_length=9, blank=True, null=True, default='No asignado')
    curso = models.CharField(max_length=255, blank=True, null=True, default='No asignado')
    
    #funcion para mostrar texto al crear o al actualizar
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.apellidos, self.DNI)
    