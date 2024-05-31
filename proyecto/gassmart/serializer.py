from rest_framework import serializers
from .models import Empresa
from .models import Usuario
from .models import Consumo
from .models import Balones

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Empresa
        fields = ('id', 'empresa', 'dirección', 'email')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ('id', 'usuario', 'empresa', 'dirección')

class ConsumoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Consumo
        fields = ('id', 'usuario', 'fecha', 'consumo', 'costo')

class BalonesSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Balones
        fields = ('id', 'empresa', 'valvula', 'peso')