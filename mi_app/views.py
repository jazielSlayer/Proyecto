from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def hola_mundo(request):
    return HttpResponse("¡Hola Mundo desde Django! 🚀")
    
# Create your views here.
def hola_mundo(request):
    return render(request, 'mi_app/inicio.html')  # Renderiza la plantilla