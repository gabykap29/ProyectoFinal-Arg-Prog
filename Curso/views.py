from django.shortcuts import render,redirect
from .models import Curso
from .models import BandaHoraria
# Create your views here.
#Vista del home
def home(request):
    cursos = Curso.objects.all()
    bandasHorarias = BandaHoraria.objects.all()
    return render(request, 'gestionCursos.html',{'cursos':cursos, 'bandasHorarias':bandasHorarias})

def bandasHorarias(request):
    bandasHorarias = BandaHoraria.objects.all()
    return render(request, 'gestionBandasHorarias.html', {'bandasHorarias': bandasHorarias})

#Vista para agregar Cursos
def agregarCursos(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        bandaHoraria_id = request.POST['bandaHoraria']
        bandaHoraria = BandaHoraria.objects.get(idBanda=bandaHoraria_id)
        
        nuevoCurso = Curso.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            bandaHoraria=bandaHoraria
        )
        
        return redirect('home')
    
    bandasHorarias = BandaHoraria.objects.all()
    return render(request, 'gestionBandasHorarias.html', {'bandasHorarias': bandasHorarias})
def editarCursos(request, id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        bandaHoraria_id = request.POST['bandaHoraria']
        bandaHoraria = BandaHoraria.objects.get(idBanda=bandaHoraria_id)
        
        nuevoCurso = Curso.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            bandaHoraria=bandaHoraria
        )
        
        return redirect('home')
    
    bandasHorarias = BandaHoraria.objects.all()
    return render(request, 'agregarCursos.html', {'bandasHorarias': bandasHorarias})

def eliminarCursos(request, id):
    Curso.objects.filter(idCurso=id).delete()
    return redirect('home')

def agregarBandaHoraria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        horaInicio = request.POST['horaInicio']
        horaFin = request.POST['horaFin']
        
        nuevaBandaHoraria = BandaHoraria.objects.create(
            nombre=nombre,
            horaInicio=horaInicio,
            horaFin=horaFin
        )
        
        return redirect('home')
    
    return render(request, 'agregarBandaHoraria.html')

def editarBandaHoraria(request, id):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        horaInicio = request.POST['horaInicio']
        horaFin = request.POST['horaFin']
        
        nuevaBandaHoraria = BandaHoraria.objects.create(
            nombre=nombre,
            horaInicio=horaInicio,
            horaFin=horaFin
        )
        
        return redirect('home')
    
    return render(request, 'agregarBandaHoraria.html')

def eliminarBandaHoraria(request, id):
    BandaHoraria.objects.filter(idBanda=id).delete()
    return redirect('home')