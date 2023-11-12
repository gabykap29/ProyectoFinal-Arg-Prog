from django.urls import path
from . import views
urlpatterns = [
    path('cursos/',views.home,name='home'),
    path('bandasHorarias/',views.bandasHorarias,name='bandasHorarias'),
    path('agregarCursos/',views.agregarCursos,name='agregarCursos'),
    path('editarCursos/<id>',views.editarCursos,name='editarCursos'),
    path('eliminarCursos/<id>/',views.eliminarCursos,name='eliminarCursos'),
    path('agregarBandaHoraria/',views.agregarBandaHoraria,name='agregarBandaHoraria'),
    path('editarBandaHoraria/<id>',views.editarBandaHoraria,name='editarBandaHoraria'),
    path('eliminarBandaHoraria/<id>/',views.eliminarBandaHoraria,name='eliminarBandaHoraria'),
]