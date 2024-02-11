from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import (
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    UpdateUserAvatarSerializer,
    UpdateUserSerializer,
)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserAvatarUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserAvatarSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
