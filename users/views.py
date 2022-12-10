from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer, SuperUserSerializer
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(APIView):
    def post(self, request: Request) -> Response:

        if request.data["is_employee"]:
            serializer = SuperUserSerializer(data=request.data)
        else:
            serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        Users = User.objects.all()
        serializer = UserSerializer(Users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    ...
