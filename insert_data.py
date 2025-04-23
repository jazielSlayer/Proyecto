import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from titulacion_proyect.models import Usuarios, Laboratorios, Categorias_Equipos, Equipos

# Insertar datos en Usuarios
Usuarios.objects.create(
    nombre="Pedro",
    apellido="Martínez",
    email="pedro.martinez@example.com",
    password="contraseña321",
    tipo_usuario="docente",
    numero_identificacion="654321987"
)

# Insertar datos en Laboratorios
Laboratorios.objects.create(
    nombre="Laboratorio de Biología",
    ubicacion="Edificio C, Piso 1",
    capacidad=20
)

# Insertar datos en Categorias_Equipos
Categorias_Equipos.objects.create(
    nombre="Computadoras",
    descripcion="Equipos de cómputo como laptops y desktops"
)

# Insertar datos en Equipos (después de crear una categoría)
categoria = Categorias_Equipos.objects.get(nombre="Computadoras")
Equipos.objects.create(
    id_categoria=categoria,
    nombre="Laptop Dell",
    descripcion="Laptop para uso en laboratorio",
    estado="disponible"
)

print("Datos insertados correctamente.")