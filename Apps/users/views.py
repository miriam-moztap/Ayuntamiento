from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer

from django.contrib.auth.models import User
from django.http import JsonResponse



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.models import User

class CreateUserView(APIView):
    authentication_classes = [JWTAuthentication]  # Aplicar autenticación JWT
    permission_classes = [AllowAny]  # Permitir a todos acceder

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generar tokens de acceso y actualización
            refresh = RefreshToken.for_user(user)

            return Response({
                'user_id': user.id,
                'email': user.email,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh)
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def post(self, request):
        email = request.POST.get('email')  # Utiliza request.POST para obtener los datos POST
        password = request.POST.get('password')

        # Crea el superusuario
        user = User.objects.create_superuser(email=email, password=password)

        return JsonResponse({'message': 'Superusuario creado exitosamente.'})

    def get(self, request):
        return JsonResponse({'error': 'Esta vista solo admite solicitudes POST.'}, status=405)