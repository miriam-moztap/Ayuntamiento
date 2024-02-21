from rest_framework import serializers
from .models import Expediente, Status
from Apps.documents.models import Document
from Apps.documents.serializers import DocExpSerializer



class StatusSerializers(serializers.ModelSerializer):

    class Meta:

        model = Status
        fields = '__all__'


class ExpedienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Expediente
        fields = '__all__'

class StatusListExpedienteSerializer(serializers.ModelSerializer):

    Expediente = serializers.SerializerMethodField()

    class Meta:

        model = Status
        fields = '__all__' ## hay que hacer el to representation con los campos


class ExpedienteStatusListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expediente
        fields = '__all__'


class ExpedienteListDocumentsSerializer(serializers.ModelSerializer):
    document = serializers.SerializerMethodField()

    class Meta:
        model = Expediente
        fields= '__all__'

    def get_document(self, obj):
        selected_documento = Document.objects.filter(expediente_id=obj.id)
        return DocExpSerializer(selected_documento, many=True).data