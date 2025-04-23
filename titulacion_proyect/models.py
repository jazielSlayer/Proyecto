from django.db import models

class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20)
    numero_identificacion = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'Usuarios'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Laboratorios(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    class Meta:
        db_table = 'Laboratorios'

    def __str__(self):
        return self.nombre

class Categorias_Equipos(models.Model):
    id = models.AutoField(primary_key=True)  # Cambiado de id_categoria a id
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Categorias_Equipos'

    def __str__(self):
        return self.nombre

class Equipos(models.Model):
    id = models.AutoField(primary_key=True)
    categoria_id = models.ForeignKey(Categorias_Equipos, on_delete=models.CASCADE, db_column='categoria_id', related_name='equipos')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20)

    class Meta:
        db_table = 'Equipos'

    def __str__(self):
        return self.nombre