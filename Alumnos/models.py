from django.db import models

# Create your models here.
#modelo del Alumno

class Alumno(models.Model):
    DNI = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()