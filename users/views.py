from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsAdmin
from .models import User
from .serializers import UserUpdateSerializer
from .serializers import UserListSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


# Admin can update user role
class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdmin]  # only admin can edit
    lookup_field = "id"  # update by user id

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAdmin]  # Only admin can access
