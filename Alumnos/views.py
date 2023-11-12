from django.shortcuts import render, redirect, get_object_or_404
from Curso.models import Curso
from django.http import JsonResponse
from .models import Alumno
# Create your views here.
def home(request):
    Alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'gestionAlumnos.html',{'Alumnos':Alumnos, 'cursos':cursos})

def registrarAlumno(request):
    nombre = request.POST['nombre']
    Apellidos = request.POST['Apellidos']
    DNI = request.POST['DNI']
    telefono = request.POST['telefono']
    email = request.POST['email']
    cursoid = request.POST['cursoid']
    curso = Curso.objects.get(idCurso = cursoid)
    
    nuevoAlumno = Alumno.objects.create(
        DNI = DNI,
        nombre = nombre,
        apellidos = Apellidos,
        telefono=telefono,
        email=email,
        cursoid=curso
    )
    return redirect('/')
def eliminarAlumno(request, DNI):
    Alumno.objects.filter(DNI = DNI).delete()
    return redirect('/')

def editarAlumno(request, DNI):
    cursos = Curso.objects.all()
    alumno = Alumno.objects.get(DNI = DNI)
    return render(request, 'editarAlumnos.html', {'alumno':alumno, 'cursos':cursos})

def guardarEdicion(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['Apellidos']
    DNI = request.POST['DNI']
    telefono = request.POST['telefono']
    email = request.POST['email']
    cursoid = request.POST['cursoid']
    curso = Curso.objects.get(idCurso = cursoid)
    
    Alumno.objects.filter(DNI = DNI).update(
        DNI = DNI,
        nombre = nombre,
        apellidos = apellidos,
        telefono = telefono,
        email = email,
        cursoid = curso
    )
    return redirect('/')

def asignarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'asignarCurso.html',{'cursos':cursos})

def asignarCursosAlumno(request):
    DNI = request.POST['DNI']
    cursoid = request.POST['cursoid']

    # Obtén el objeto Alumno o devuelve un error 404 si no se encuentra
    alumno = get_object_or_404(Alumno, DNI=DNI)

    # Obtén el objeto Curso o devuelve un error 404 si no se encuentra
    curso = get_object_or_404(Curso, idCurso=cursoid)

    # Asigna el curso al alumno
    alumno.cursoid = curso

    # Guarda los cambios
    alumno.save()

    return redirect('/')



#obtener los alumnos por curso en formato JSON
def alumnos_por_curso(request, cursoid):
    curso = get_object_or_404(Curso, idCurso=cursoid)
    alumnos = Alumno.objects.filter(cursoid=curso)

    # Preparar la información de los alumnos en formato JSON
    alumnos_data = [
        {
            'DNI': alumno.DNI,
            'nombre': alumno.nombre,
            'apellidos': alumno.apellidos,
            'email': alumno.email,
            'telefono': alumno.telefono,
        }
        for alumno in alumnos
    ]

    return JsonResponse(alumnos_data, safe=False)


#Vista para mostrar los alumnos por curso

def alumnosPorCurso(request,cursoid):
    return render(request, 'alumnosCursos.html')