from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .serializers import RegisterUserSerializer, LoginSerializer, UserSerializer, LoginLogbookSerializer
from .models import LoginLogbook, User



#Este código lo modificaré para que sólo el super usuario pueda crear otros usuarios
class CreateNewUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] #sólo el superusuario puede crear usuarios

    def post(self, request):
        #Verificar si el usuario autenticado es superusuario
        if not request.user.role_id != 1:
            return Response({'error': 'No tienes permiso para crear usuarios'}, status=status.HTTP_403_FORBIDDEN)

        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'msg':'usuario registrado exitosamente','user_id': serializer.instance.id}, status=status.HTTP_201_CREATED)



class LoginAndRegisterUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user) ##aquí tengo que hacer que el refresh se utilice solamente para cuando pierden su password
            access_token = str(refresh.access_token)
            login_record = LoginLogbook.objects.create(user=user)
            return Response({
                'access': access_token
            
            })
        else:
            return Response({'error': 'Credenciales inválidas'}, status=400)
        
        