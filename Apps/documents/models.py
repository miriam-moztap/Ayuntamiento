from django.db import models
import os
from decouple import config
from django.core.exceptions import ValidationError
from Apps.Areas.models import Subdepartamento, Departamento
from Apps.expedientes.models import Expediente

class Tipo_Documento(models.Model):
    name = models.CharField(max_length=255, null=False,
                            verbose_name="Tipo_Documento")
    description = models.CharField(
        max_length=555, null=True, verbose_name="Descripcion")

    class Meta:
        verbose_name = 'Tipo_Documento'
        verbose_name_plural = 'Tipo_Documentos'
        db_table = 'Tipo_Documento'
        ordering = ('id',)

    def __str__(self):
        return self.name

def validar_archivo_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Solo se permiten archivos PDF, JPG y PNG.')



class Document(models.Model):
    
    nombre_del_documento = models.CharField(max_length=255, null=False, verbose_name='Nombre del documento')
    nombre_de_quien_entrega = models.CharField(max_length=100, null=False, verbose_name='Nombre de quien entrega')
    status_delete = models.BooleanField(default=False, null=False, verbose_name='status')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')
    archivo = models.FileField(upload_to=os.environ.get('MEDIA')+'archivos/', validators=[validar_archivo_extension], null=True) #*******utilizar con variable de entorno de path
    nombre_de_quien_carga = models.CharField(max_length=100, null=False, verbose_name='Nombre de quien carga')
    tipoDocumento = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, related_name="Tipo_Documento", default='', null=True)
    expediente= models.ForeignKey(Expediente, on_delete=models.CASCADE, default='', null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'
        db_table = 'Document'
        ordering = ('id',)


class DocDep(models.Model):
    name = models.CharField(max_length=255, null=False, verbose_name="DocDep")
    departamento = models.ForeignKey(
        Departamento, related_name="Departamento", on_delete=models.CASCADE)
    subdepartamento = models.ForeignKey(
        Subdepartamento, related_name="Subdepartamento", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'DocDep'
        verbose_name_plural = 'DocDeps'
        db_table = 'DocDep'
        ordering = ('id',)

    def __str__(self):
        return self.name


class sharedlinks(models.Model):
    linked_document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name='documentos', default="", verbose_name="Documento Vinculado")
    urldocumento = models.CharField(
        max_length=255, null=False, default="", verbose_name="Url Documento")

    class Meta:
        verbose_name = 'sharedlinks'
        verbose_name_plural = 'sharedlinks'
        db_table = 'sharedlinks'
        ordering = ('id',)
