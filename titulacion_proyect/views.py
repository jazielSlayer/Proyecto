from rest_framework import generics
from rest_framework.permissions import AllowAny  # Añadido
from .models import Usuarios, Laboratorios, Categorias_Equipos, Equipos
from .serializers import UsuariosSerializer, LaboratoriosSerializer, CategoriasEquiposSerializer, EquiposSerializer

# Vista para Usuarios
class UsuariosRegisterView(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

# Vista para Laboratorios
class LaboratoriosCreateView(generics.CreateAPIView):
    queryset = Laboratorios.objects.all()
    serializer_class = LaboratoriosSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

# Vista para Categorias_Equipos
class CategoriasEquiposCreateView(generics.CreateAPIView):
    queryset = Categorias_Equipos.objects.all()
    serializer_class = CategoriasEquiposSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación

# Vista para Equipos
class EquiposCreateView(generics.CreateAPIView):
    queryset = Equipos.objects.all()
    serializer_class = EquiposSerializer
    permission_classes = [AllowAny]  # Permitir acceso sin autenticación