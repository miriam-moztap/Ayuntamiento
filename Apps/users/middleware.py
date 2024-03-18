from django.middleware.csrf import get_token
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CSRFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si es una solicitud segura (POST, PUT, PATCH, DELETE)
        if request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            # Verificar si la vista es CreateUserView (o cualquier otra vista que necesites proteger con CSRF)
            if request.path == 'login/' or request.path == 'login/':
                # Obtener el token CSRF y verificar si está presente en la solicitud
                csrf_token = get_token(request)
                if not request.META.get('HTTP_X_CSRFTOKEN') == csrf_token:
                    # Devolver una respuesta de error si el token CSRF no coincide
                    return JsonResponse({'detail': 'CSRF Token no válido'}, status=status.HTTP_403_FORBIDDEN)
        # Si no hay problemas con el token CSRF, continuar con la vista normalmente
        response = self.get_response(request)
        return response
