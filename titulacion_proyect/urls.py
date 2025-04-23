from django.urls import path
from .views import UsuariosRegisterView, LaboratoriosCreateView, CategoriasEquiposCreateView, EquiposCreateView

urlpatterns = [
    path('users/register/', UsuariosRegisterView.as_view(), name='users-register'),
    path('laboratorios/create/', LaboratoriosCreateView.as_view(), name='laboratorios-create'),
    path('categorias-equipos/create/', CategoriasEquiposCreateView.as_view(), name='categorias-equipos-create'),
    path('equipos/create/', EquiposCreateView.as_view(), name='equipos-create'),
]