from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Empresa, Usuario, Consumo, Balones
from .serializer import EmpresaSerializer, UsuarioSerializer, ConsumoSerializer, BalonesSerializer

class EmpresaListView(APIView):
    
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmpresaDetailView(APIView):
    
    def get(self, request, empresa_id):
        empresa = Empresa.objects.get(pk=empresa_id)
        serializer = EmpresaSerializer(empresa)
        return Response(serializer.data)
    
    def put(self, request, empresa_id):
        empresa = Empresa.objects.get(pk=empresa_id)
        serializer = EmpresaSerializer(empresa, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, empresa_id):
        empresa = Empresa.objects.get(pk=empresa_id)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UsuarioListView(APIView):
    
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UsuarioDetailView(APIView):
    
    def get(self, request, usuario_id):
        usuario = Usuario.objects.get(pk=usuario_id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    
    def put(self, request, usuario_id):
        usuario = Usuario.objects.get(pk=usuario_id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, usuario_id):
        usuario = Usuario.objects.get(pk=usuario_id)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ConsumoListView(APIView):
    
    def get(self, request):
        consumos = Consumo.objects.all()
        serializer = ConsumoSerializer(consumos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ConsumoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConsumoDetailView(APIView):
    
    def get(self, request, consumo_id):
        consumo = Consumo.objects.get(pk=consumo_id)
        serializer = ConsumoSerializer(consumo)
        return Response(serializer.data)
    
    def put(self, request, consumo_id):
        consumo = Consumo.objects.get(pk=consumo_id)
        serializer = ConsumoSerializer(consumo, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, consumo_id):
        consumo = Consumo.objects.get(pk=consumo_id)
        consumo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BalonesListView(APIView):
    
    def get(self, request):
        balones = Balones.objects.all()
        serializer = BalonesSerializer(balones, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BalonesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BalonesDetailView(APIView):
    
    def get(self, request, balones_id):
        balones = Balones.objects.get(pk=balones_id)
        serializer = BalonesSerializer(balones)
        return Response(serializer.data)
    
    def put(self, request, balones_id):
        balones = Balones.objects.get(pk=balones_id)
        serializer = BalonesSerializer(balones, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, balones_id):
        balones = Balones.objects.get(pk=balones_id)
        balones.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)