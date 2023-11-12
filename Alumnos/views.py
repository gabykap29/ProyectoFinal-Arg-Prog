from django.shortcuts import render, redirect
from .models import Alumno
# Create your views here.
def home(request):
    Alumnos = Alumno.objects.all()
    return render(request, 'gestionAlumnos.html',{'Alumnos':Alumnos})

def registrarAlumno(request):
    nombre = request.POST['nombre']
    Apellidos = request.POST['Apellidos']
    DNI = request.POST['DNI']
    telefono = request.POST['telefono']
    email = request.POST['email']
    curso = request.POST['curso']
    nuevoAlumno = Alumno.objects.create(
        DNI = DNI,
        nombre = nombre,
        apellidos = Apellidos,
        telefono=telefono,
        email=email,
        curso=curso
    )
    return redirect('/')
def eliminarAlumno(request, DNI):
    Alumno.objects.filter(DNI = DNI).delete()
    return redirect('/')

def editarAlumno(request, DNI):
    alumno = Alumno.objects.get(DNI = DNI)
    return render(request, 'editarAlumnos.html', {'alumno':alumno})

