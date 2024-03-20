from rest_framework import serializers
from .models import LoginLogbook, User
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import Role,  Usuario

# class RoleSerializer(serializers.ModelSerializer):

#     class Meta():
#         model = Role
#         fields = ['id', 'name', 'description']

# class UserRoleSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Usuario
#         fields = ['name', 'last_name', 'email', 'phone', 'role']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# class SuperUser(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['name', 'password', 'email', 'role']

# from django.contrib.auth.models import User



#este código lo voy a dejar para que el superusuario lo use al crear a otros usuarios, y 
#en caso de que el usuario se repita, mande el error necesaario.

from rest_framework import serializers

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    
    def create(self, validated_data):
        name = validated_data['name']
        if User.objects.filter(name=name).exists():
            raise serializers.ValidationError({"error": "Este nombre de usuario ya existe"})
        
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'role', 'password']

#_______________________________________________________________________________________________##
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=50)
    #username =serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    # token = serializers.CharField(max_length=5000)


class LoginLogbookSerializer(serializers.Serializer):
    class Meta:
        model = LoginLogbook
        fields = '__all__'