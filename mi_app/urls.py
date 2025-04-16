from django.urls import path
from . import views

urlpatterns = [
    path('', views.hola_mundo, name='hola_mundo'),
    path('registro/estudiante/', views.registro_estudiante, name='registro_estudiante'),
    path('registro/docente/', views.registro_docente, name='registro_docente'),
]