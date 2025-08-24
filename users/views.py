from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .serializers import UserRegisterSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from users.permissions import IsAdmin
from .models import User
from .serializers import UserUpdateSerializer
from .serializers import UserListSerializer
from rest_framework.permissions import IsAuthenticated


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
    

class GetUserByUsernameView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            serializer = UserListSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


            