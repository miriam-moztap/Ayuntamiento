from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import status
from rest_framework import generics
from .serializers import DocumentSerializer,Tipo_DocumentoSerializer
from .models import Document, Tipo_Documento


# Post para almacenar un documento en tabla de documentos
class DocumentAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser, JSONParser)

    def post(self, request):
        print(request.data)
        try:
            file = request.data['archivo']
            request.data['archivo'] = file
        except KeyError:
            file = None  
        serializer = DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class SingleDocumentAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        document = Document.objects.filter(id=id).first()
        if document is None:
            return Response('No se encontró el documento', status=status.HTTP_400_BAD_REQUEST)
        serializer = DocumentSerializer(document)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, id):
        document = Document.objects.filter(id=id).first()
        if document is None:
            return Response('No se encontró el documento', status=status.HTTP_400_BAD_REQUEST)
        serializer = DocumentSerializer(
            document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('no se pudieron guardar los cambios', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        document = Document.objects.filter(id=id).filter()
        if document is None:
            return Response('No se encontro el documento para eliminar', status=status.HTTP_400_BAD_REQUEST)
        document.delete()
        return Response('documento eliminado Sastifactorimente', status=status.HTTP_200_OK)
    
class TipoDocumentoListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tipos_documentos = Tipo_Documento.objects.all()
        serializer = Tipo_DocumentoSerializer(tipos_documentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TipoDocumentoDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            tipo_documento = Tipo_Documento.objects.get(pk=pk)
            serializer = Tipo_DocumentoSerializer(tipo_documento)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Tipo_Documento.DoesNotExist:
            return Response({'error': 'Tipo de documento no encontrado'}, status=status.HTTP_404_NOT_FOUND)