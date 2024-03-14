import os
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from Apps.users.models import User
from django.contrib.auth.models import User

class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if email is None or password is None:
            return Response({'message': 'El email y la contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'No hay usuario con el email dado'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(password):
            return Response({'message': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

        # Generar el token JWT
        token_payload = {
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=1)  # Cambia la expiración según tus necesidades
        }
        token = jwt.encode(token_payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        # Actualizar la última fecha de inicio de sesión del usuario
        user.last_login = datetime.now()
        user.save()

        return Response({'token': token.decode('utf-8')}, status=status.HTTP_200_OK)
