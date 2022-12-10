from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer, LoginSerializer, SuperUserSerializer
from .models import User
from django.contrib.auth import authenticate


class RegisterView(APIView):
    def post(self, request: Request) -> Response:

        if request.data['is_employee']:
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


class LoginView(APIView):
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'])

            if not user:
                return Response({'detail': 'invalid login'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'detail': 'login'}, status=status.HTTP_202_ACCEPTED)
            
            
            
