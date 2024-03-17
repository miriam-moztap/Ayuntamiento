from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.postgres.fields import ArrayField
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.conf import settings

# Models
from Apps.users.choices import roles

# Utils
# from Apps.users.utils import send_email_validation

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


class UserManager(BaseUserManager): ##esta clase es la forma en la que queremos que se cree el usuario y el superusuario.

    def create_user(self, name, last_name, email, role_id, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')
        
        user = self.model(
            name=name,
            last_name=last_name,
            role_id=role_id,
            email=self.normalize_email(email),
            # is_active=True,
            # is_superuser=False,
            # is_staff=False,
            # status_delete=False,
            # **extra_fields,
        )
        # if password:
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, last_name, role_id, password):
        if not email:
            raise ValueError('El superusuario debe tener un correo electrónico')
        
        user = self.create_user(
            email,
            name,
            last_name,
            role_id=role_id,
            password=password,
            
            # is_active=True,
            # is_superuser=True,
            # is_staff=True,
            
            # **extra_fields,
        )
        user.user_administrador=True
        # user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        unique=True, max_length=100, null=False, verbose_name='email', default='')
    name = models.CharField(max_length=150, null=True, verbose_name='name', default='')
    last_name = models.CharField(
        max_length=150, null=True, verbose_name='last name', default='')
    phone = models.CharField(verbose_name='phone', null=True, max_length=20, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_administrator = models.BooleanField(default = False)
    status_delete = models.BooleanField(default=False)
    role = models.ForeignKey(Role, choices=roles, on_delete=models.CASCADE, null=True, default='')
    hidden_fields = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    objects = UserManager()

    # groups = models.ManyToManyField('auth.Group',
    #     verbose_name='groups',
    #     related_name='usuarios_related',
    #     blank=True,
    #     help_text='Los grupos a los que pertenece este usuario.'
    # )
    # user_permissions = models.ManyToManyField('auth.Permission',
    #     verbose_name='user permissions',
    #     related_name='usuarios_related',
    #     blank=True,
    #     help_text='Permisos específicos para este usuario.'
    # )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'last_name', 'role_id']

    def __str__(self):
        return f'{self.id} - {self.name} ({self.email})'
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.user_administrador
    # class Meta:
    #     verbose_name = 'User'
    #     verbose_name_plural = 'Users'
    #     db_table = 'user'
    #     ordering = ('id',)


#modelo para registrar cada vez que alguien se loguea
    
class LoginRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    login_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'LoginRegister'

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"