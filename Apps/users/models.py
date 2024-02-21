from django.db import models
from Apps.users.choices import roles
# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name='Name', default='')
    description = models.CharField(
        max_length=255, null=False, verbose_name='Description', default='')
    isSuperAdmin = models.BooleanField(
        default=False, verbose_name='Administrador')
    status_delete = models.BooleanField(
        default=False, verbose_name='Status Delete')
    host = models.CharField(max_length=100, null=True,
                            verbose_name='Host access', default='')

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
        db_table = 'role'
        ordering = ('id', )

        def __str__(self):
            return self.name
    

class User(models.Model):
    username = models.CharField(max_length=150, null=True, verbose_name='name', default='')
    last_name = models.CharField(
        max_length=150, null=True, verbose_name='last name', default='')
    email = models.EmailField(
        unique=True, max_length=100, null=False, verbose_name='email', default='')
    phone = models.CharField(verbose_name='phone', null=True, max_length=20, default='')
    role = models.ForeignKey(Role, choices=roles, on_delete=models.CASCADE, default='')
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        ordering = ('id',)

    def _str_(self):
        return self.username