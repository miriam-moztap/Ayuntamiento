# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import AllowAny

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



from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer, LoginSerializer
from .models import LoginRegister

# Create your views here.

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'msg':'usuario registrado'}, status=status.HTTP_201_CREATED)
    
        

class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']

        user = authenticate(username=username, password=password, email=email)
        
        if user is None:
            return Response({'error': 'Credenciales no válidas'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Guarda el registro de inicio de sesión en la base de datos
        login_record = LoginRegister.objects.create(user=user)
        
        # Devuelve la respuesta con los datos del usuario autenticado
        data = {
            'id': user.id,
            'username': user.username,
            # Agrega otros campos según sea necesario
        }

        return Response(data, status=status.HTTP_200_OK)

