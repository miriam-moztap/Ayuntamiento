# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

# from .models import Usuario
# from .serializers import UserSerializer

# from django.contrib.auth.models import User
# from django.http import JsonResponse



# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import JsonResponse
# from django.contrib.auth.models import User

# class CreateUserView(APIView):
#     authentication_classes = [JWTAuthentication]  # Aplicar autenticación JWT
#     permission_classes = [AllowAny]  # Permitir a todos acceder

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()

#             # Generar tokens de acceso y actualización
#             refresh = RefreshToken.for_user(user)

#             return Response({
#                 'user_id': user.id,
#                 'email': user.email,
#                 'access_token': str(refresh.access_token),
#                 'refresh_token': str(refresh)
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CreateSuperUserView(APIView):    
#     def post(self, request):
#         email = request.POST.get('email')  # Utiliza request.POST para obtener los datos POST
#         password = request.POST.get('password')

#         # Crea el superusuario
#         user = User.objects.create_superuser(email=email, password=password)

#         return JsonResponse({'message': 'Superusuario creado exitosamente.'})


#from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .serializers import RegisterUserSerializer, LoginSerializer, UserSerializer
from .models import LoginRegister, User



#Este código lo modificaré para que sólo el super usuario pueda crear otros usuarios
class CreateNewUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'usuario registrado'}, status=status.HTTP_201_CREATED)
    
        

from rest_framework_simplejwt.tokens import AccessToken

class LoginAndRegisterUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({
                'refresh': str(refresh),
                'access': access_token,
            })
        else:
            return Response({'error': 'Credenciales inválidas'}, status=400)
        # # Guardar el registro de inicio de sesión en la base de datos
        # login_record = LoginRegister.objects.create(user=user)
        
        # # Devolver la respuesta con los datos del usuario autenticado
        # return Response(response, status=status.HTTP_200_OK)




# def post(self, request):
    #     email = request.data.get('email')
    #     password = request.data.get('password')
        
    #     if not email or not password:
    #         return Response({'message': 'El email y la contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return Response({'message': 'No hay usuario con el email proporcionado'}, status=status.HTTP_400_BAD_REQUEST)

    #     if not user.check_password(password):
    #         return Response({'message': 'La combinación de email y contraseña es incorrecta'}, status=status.HTTP_400_BAD_REQUEST)

    #     if not user.is_active:
    #         return Response({'message': 'La cuenta de usuario no está activa'}, status=status.HTTP_400_BAD_REQUEST)

    #     access_token = AccessToken.for_user(user)
    #     user_serializer = UserSerializer(user)
        
    #     response = {
    #         'token': str(access_token),
    #         'user': user_serializer.data
    #     }
        


class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # username = serializer.data['username']
        email = serializer.data['email']
        password =serializer.data['password']
        

        user = authenticate( email = email, password = password)
        
        if user:
            print(email)
            print(password)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response('fallaste', status=status.HTTP_400_BAD_REQUEST)
    '''{
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },'''
       
       
       
        # data = {
        #     'id': user.id,
        #     'username': user.username
        
        # }

        # return Response(data, status=status.HTTP_200_OK)