# users/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # role removed

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role='participant'   # default role
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Serializer for Admin to edit role
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']  # admin can change role
        extra_kwargs = {
            "username": {"required": False},
            "email": {"required": False},
            "role": {"required": False}
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'is_active', 'is_superuser']




