from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from users.models import Role

class Command(BaseCommand):
    help = 'Crea un superusuario con el rol de administrador'

    def handle(self, *args, **options):
        username = input('Nombre: ')
        email = input('Correo electrónico: ')
        password = input('Contraseña: ')

        # Crear el superusuario
        user = User.objects.create_user(username=username, email=email, password=password)

        # Obtener el rol de administrador
        admin_role = Role.objects.get(name='Administrador')

        # Asignar el rol de administrador al superusuario
        user.role = admin_role
        user.is_superuser = True  # Marcar como superusuario
        user.is_staff = True  # Marcar como miembro del staff
        user.save()

        self.stdout.write(self.style.SUCCESS('Superusuario creado con éxito con el rol de administrador.'))
