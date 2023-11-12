from django.db import models

# Create your models here.
class BandaHoraria(models.Model):
    idBanda = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()



class Curso(models.Model):
    idCurso = models.IntegerField(primary_key=True)
    nombre= models.CharField(max_length=255)
    bandaHoraria = models.ForeignKey(BandaHoraria, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255)
    
