from rest_framework import serializers

from .models import Document
from .models import Tipo_Documento



class Tipo_DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Documento
        fields = '__all__'


        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        

class DocExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields= (
            'id',
            'nombre_del_documento',
            'archivo',
            'tipoDocumento',
        )


class DocDepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'