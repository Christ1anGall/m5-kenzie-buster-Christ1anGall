from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    birthdate = serializers.DateField(allow_null=False)
    is_employee = serializers.BooleanField(),
    is_superuser = serializers.BooleanField(read_only=True),

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class SuperUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=127)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)

    birthdate = serializers.DateField(allow_null=False)
    is_employee = serializers.BooleanField(),
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):

        user = User.objects.create_superuser(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    is_superuser = serializers.CharField(read_only=True),
    password = serializers.CharField(write_only=True)