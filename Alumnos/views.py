from django.shortcuts import render
from .models import Alumno
# Create your views here.
def home(request):
    Alumnos = Alumno.objects.all()
    return render(request, 'gestionAlumnos.html',{'Alumnos':Alumnos})