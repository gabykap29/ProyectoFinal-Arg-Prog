from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('cargarAlumnos/', views.cargar_alumnos_desde_csv, name='cargar_alumnos_desde_csv'),
    path('registrarAlumno/',views.registrarAlumno,name='registrarAlumno'),
    path('asignarCursos/',views.asignarCursos,name='asignarCursos'),
    path('asignarCursosAlumno/',views.asignarCursosAlumno,name='asignarCursosAlumno'),
    path('guardarEdicion/',views.guardarEdicion,name='guardarEdicion'),
    path('editarAlumnos/<DNI>',views.editarAlumno,name='editarAlumno'),
    path('api/alumnosPorCurso/<cursoid>/', views.alumnos_por_curso, name='asignarCursosAlumno'),
    path('alumnosPorCurso/<cursoid>/', views.alumnosPorCurso, name='alumnosPorCurso'),
    path('eliminarAlumno/<DNI>/',views.eliminarAlumno,name='eliminarAlumno'),
]