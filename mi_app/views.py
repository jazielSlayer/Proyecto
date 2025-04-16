from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EstudianteForm, DocenteForm

def hola_mundo(request):
    return render(request, 'mi_app/inicio.html')

def registro_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hola_mundo')
    else:
        form = EstudianteForm()
    return render(request, 'mi_app/form_estudiante.html', {'form': form})

def registro_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hola_mundo')
    else:
        form = DocenteForm()
    return render(request, 'mi_app/form_docente.html', {'form': form})