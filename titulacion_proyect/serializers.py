from rest_framework import serializers
from .models import Usuarios, Laboratorios, Categorias_Equipos, Equipos

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class LaboratoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorios
        fields = '__all__'

class CategoriasEquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias_Equipos
        fields = '__all__'

class EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipos
        fields = '__all__'