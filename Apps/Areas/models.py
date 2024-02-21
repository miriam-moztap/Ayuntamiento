from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, null=False, verbose_name="Departamento")
    description = models.CharField(
        max_length=555, null=True, verbose_name="Description")

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'Departamento'
        ordering = ('id',)
    def __str__(self):
        return self.nombre

class Subdepartamento(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

# Create your models here.
