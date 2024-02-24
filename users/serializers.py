from typing import Dict, Any

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User
from django.contrib.auth import authenticate, login


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, str]:
        data = super().validate(attrs)
        user = User.objects.get(username=attrs['username'])

        data.update(**dict(attrs))
        data['avatar'] = user.avatar.url if user.avatar else ''
        return data

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username

        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
        error_messages={
            'unique': 'Email must be unique'
        }
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('pk', 'username', 'password', 'password2', 'email')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UpdateUserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'avatar')


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk',  'username', 'email', 'password')

    def update(self, instance, validated_data):
        print(validated_data)
        instance.username = validated_data['username']
        instance.email = validated_data['email']
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'avatar']