from django.db import models
from Curso.models import Curso
# Create your models here.
#modelo del Alumno

class Alumno(models.Model):
    DNI = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField( blank=True, null=True, default='No asignado')
    telefono= models.CharField(max_length=9, blank=True, null=True, default='No asignado')
    cursoid = models.ForeignKey(Curso, on_delete=models.CASCADE, default=1)
    #funcion para mostrar texto al crear o al actualizar
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.apellidos, self.DNI)
    