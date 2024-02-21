from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import User, Role
from .serializers import RoleSerializer, UserSerializer, UserRoleSerializer


class CreateListUser(APIView):

    def post(self, request):
        data = request.data.copy()
        role = data.get('role', None)
        if role is None:
            return Response({'message': 'El rol es requerido'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("message: Usuario creado", status=status.HTTP_200_OK) ##user.data, usar este código para el envío del token al email del usuario

class ListUpdateDeleteUser(APIView):

    def get(self, request, id):
        user = User.objects.all()
        serializer = UserSerializer(serializer.data)
    
