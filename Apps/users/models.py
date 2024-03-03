from django.db import models
from django.contrib.auth.models import User
from Apps.users.choices import roles
from django.apps import AppConfig
# from django.db.models.signals import post_init
# from django.conf import settings
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.contrib.postgres.fields import ArrayField

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
    


# # Utils
# # from API.general.choices import roles
# # from API.general.utils import send_email_validation
# # from .choices import status_user





# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.db import models
# from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Create and return a superuser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)

#     def create_admin_user(self, email, password=None, **extra_fields):
#         """
#         Create and return an admin user with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', False)  # Not a superuser
#         return self.create_user(email, password, **extra_fields)



# class Usuario(AbstractBaseUser, PermissionsMixin):

#     name = models.CharField(
#         max_length=150, null=True, verbose_name='name',)
#     lastname = models.CharField(
#         max_length=150, null=True, verbose_name='lastname',)
    
#     email = models.EmailField(
#         unique=True, max_length=100, null=False, verbose_name='email',)
#     token = models.CharField(max_length=40, null=True, default=None)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     status_delete = models.BooleanField(default=False)
#     role = models.ForeignKey(Role, choices=roles, on_delete=models.CASCADE)
    
#     #hidden_fields = ArrayField(models.CharField(max_length=50), blank=True, default=[])
    

#     USERNAME_FIELD = 'email'
#     objects = UserManager()

#     class Meta:
#         verbose_name = 'Usuario'
#         verbose_name_plural = 'Usuarios'
#         db_table = 'usuarios'
#         ordering = ('id',)

#     def __str__(self):
#         return f'{self.name} {self.email}'
#     # @staticmethod
#     # def email_message(subject, url, user, password, html):
#     #     message = render_to_string(html, {
#     #         'user': user.name if user.name else 'Usuario',
#     #         'email': user.email,
#     #         'password': password,
#     #         'url': url,
#     #         'uid': urlsafe_base64_encode(force_bytes(user.id)),
#     #         'token': user.token,
#     #         'app_name': settings.APP_NAME
#     #     })
#     #     send_email_validation(subject, [user.email], message)
#     #     return True

#     # @ staticmethod
#     # def search_account(uidb64):
#     #     try:
#     #         uid = force_bytes(urlsafe_base64_decode(uidb64)).decode()
#     #         user = User.objects.get(id=uid)
#     #     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#     #         user = None
#     #     return user

#     # @ staticmethod
#     # def search_account_email(email):
#     #     try:
#     #         user = User.objects.get(email=email, status_delete=False)
#     #     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#     #         user = None
#     #     return user



class LoginRegister(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    login_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'LoginRegister'

    def __str__(self):
        return f"{self.user.username} - {self.login_time}"