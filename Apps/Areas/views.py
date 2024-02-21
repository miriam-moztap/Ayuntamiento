from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepartamentoSerializer
from django.http import Http404
from .models import Departamento
from .serializers import DepartamentoListSubdepartamentosSerializer

class DepartamentoListAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)
    
class DepartamentoDetail(APIView):
    def get_object(self, pk):
        try:
            return Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)

    def patch(self, request, pk):
        departamento = self.get_object(pk)
        serializer = DepartamentoSerializer(departamento, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        departamento = self.get_object(pk)
        departamento.delete()
        return Response("message: departamento eliminado satifactoriamente", status=status.HTTP_204_NO_CONTENT)
    
class DepartamentoListSubdepartamentosView(APIView):
    def get(self, request, *args, **kwargs):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoListSubdepartamentosSerializer(departamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)