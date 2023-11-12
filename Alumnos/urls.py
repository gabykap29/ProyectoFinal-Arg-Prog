from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registrarAlumno/',views.registrarAlumno,name='registrarAlumno'),
    path('editarAlumno/<DNI>',views.editarAlumno,name='editarAlumno'),
    path('eliminarAlumno/<DNI>/',views.eliminarAlumno,name='eliminarAlumno'),
]