from rest_framework import serializers
from .models import Role,  User

class RoleSerializer(serializers.ModelSerializer):

    class Meta():
        model = Role
        fields = ['id', 'name', 'description']

class UserRoleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'phone', 'role']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    