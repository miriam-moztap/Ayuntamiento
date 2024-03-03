from django.db import models
from django.contrib.auth.models import User
# from Apps.users.models import Usuario
from Apps.Areas.models import Departamento


# Create your models here.

class Status(models.Model):
    status = models.CharField(
        max_length=100, blank=False, default="", verbose_name="Status")
    descripcion_status = models.CharField(
        max_length=255, blank=False, default="", verbose_name="Descripcion del Status")

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        db_table = 'Status'
        ordering = ('id',)


class Expediente(models.Model):
    numero_expediente = models.CharField(
        max_length=100, blank=False, default="", verbose_name="Numero de Expediente")
    nombre_remitente = models.CharField(
        max_length=100, blank=False, default="", verbose_name="Nombre del Remitente")
    fecha_creacion = models.DateField(
        auto_now_add=True, verbose_name="Fecha de Creacion")
    plazo_para_responder = models.DateField(
        blank=False, verbose_name="Plazo para Responder")
    numero_copias = models.IntegerField(
        default=0, verbose_name="Numero de Copias")
    numero_anexos = models.IntegerField(
        default=0, verbose_name="Numero de Anexos")
    fecha_de_cierre = models.DateField(
        blank=False, verbose_name="Fecha de Cierre")
    monto = models.FloatField(blank=False, verbose_name="Monto")
    abogado = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuario_id')
    area = models.ForeignKey(
        Departamento, on_delete=models.CASCADE, verbose_name='area_id')
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, verbose_name='status_id')


    class Meta:
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'
        db_table = 'Expedientes'
        ordering = ('id',)
