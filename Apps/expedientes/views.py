from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Expediente
from .serializers import ExpedienteSerializer, ExpedienteListDocumentsSerializer

# Create your views here.
# falta modificar el crud para cuando esté listo el login, pues se tienen que dar permisos para expediente, documento y áreas.
class ExpedienteAPIView(APIView): ##Una vez creado el login, se debe modificar para que solo cierto(s) roles puedan crear un expediente
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        if request.method == "POST":
            serializer = ExpedienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        expedientes = Expediente.objects.all()
        serializer = ExpedienteSerializer(expedientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SingleExpedienteAPIGetUpdateDeleteView(APIView): 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
       
    def get(self, request, id):
        expediente = Expediente.objects.filter(id=id).first()
        if expediente is None:
            return Response({'No se encontró el expediente'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpedienteListDocumentsSerializer(expediente) #(data=request.data, partial=True) esto no se pone porque no es adquí donde se edita el lugar jeje
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        expediente = Expediente.objects.filter(id=id).first()
        if expediente is None:
            return Response('No se encontró el documento', status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpedienteSerializer(
            expediente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('no se pudieron guardar los cambios', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        expediente =Expediente.objects.filter(id=id).filter()
        if expediente is None:
            return Response('No se encontro el expediente para eliminar', status=status.HTTP_400_BAD_REQUEST)
        expediente.delete()
        return Response('expediente eliminado Sastifactorimente', status=status.HTTP_200_OK)
