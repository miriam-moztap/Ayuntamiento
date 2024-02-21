from rest_framework import serializers
from .models import Departamento, Subdepartamento

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class SubdepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subdepartamento
        fields = '__all__'

class DepartamentoListSubdepartamentosSerializer(serializers.ModelSerializer):
    subdepartamentos = serializers.SerializerMethodField()

    class Meta:
        model = Departamento
        fields = '__all__'

    def get_subdepartamentos(self, obj):
        selected_subdepartamentos = Subdepartamento.objects.filter(departamento_id=obj.id)
        return SubdepartamentoSerializer(selected_subdepartamentos, many=True).data

